import requests
import csv

# Define the base URL of the Ajio API and create an empty list for results
base_url = "https://www.ajio.com/api/search"
results = []

for page in range(1, 500):

    # Set the parameters for the API request
    params = {
        "fields": "SITE",
        "currentPage": page,
        "pageSize": 500,
        "format": "json",
        "query": "shirt:relevance",
        "sortBy": "relevance",
        "text": "shirt",
        "gridColumns": 3,
        "advfilter": "true",
        "platform": "Desktop",
        "is_ads_enable_plp": "true",
        "is_ads_enable_slp": "true",
        "showAdsOnNextPage": "true",
        "displayRatings": "true",
        "segmentIds": ""
    }

    # Send a GET request to the Ajio API
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Check if the 'products' key exists in the response data
        if 'products' in data:
            products = data['products']

            # Iterate through the list of products
            for product in products:
                alt_text = product.get('images')[0].get('altText')
                # brand_name = product.get('fnlProductData').get('brandName')
                price = product.get('price').get('formattedValue')
                mrp = product.get('wasPriceData').get('formattedValue')
                
                # Calculate the discount percentage if both MRP and price are available
                if mrp and price:
                    mrp_value = float(mrp.replace('Rs.', '').replace(',', '').strip())
                    price_value = float(price.replace('Rs.', '').replace(',', '').strip())
                    discount_percent = ((mrp_value - price_value) / mrp_value) * 100
                else:
                    discount_percent = None
                
                url = "https://www.ajio.com" + product.get('url')
                
                # Extract image URLs from the product data
                image_urls = [image['url'] for image in product.get('images')]
                
                # Create a dictionary for each product and add it to the results list
                result = {
                    "Alt Text": alt_text,
                    # "Brand Name": brand_name,
                    "Price (INR)": price,
                    "MRP (INR)": mrp,
                    "Discount (%)": discount_percent,
                    "URL": url,
                    "Image URLs": image_urls
                }
                results.append(result)

        else:
            print("Response format is not as expected")

    else:
        print(f"API request failed with status code: {response.status_code}")

    # Save the extracted data to a CSV file
    with open("ajio_shirt_products.csv", "w", newline='', encoding="utf-8") as csvfile:
        fieldnames = ["Alt Text", "Price (INR)", "MRP (INR)", "Discount (%)", "URL", "Image URLs"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        # Write each product's data to the CSV file
        for product in results:
            writer.writerow(product)

    print("done : " , page)

print("Data has been saved")

