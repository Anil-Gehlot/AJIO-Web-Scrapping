import requests
import csv

# Define the base URL of the Ajio API and create an empty list for results
base_url = "https://www.ajio.com/api/category/83"
results = []

for page in range(500):

    # Set the parameters for the API request for jackets
    params = {
        "currentPage": page,  # Specify the desired page number
        "pageSize": 40,
        "format": "json",
        "query": "%3Arelevance",
        "sortBy": "relevance",
        "curated": "true",
        "curatedid": "jackets-4271-38471",
        "gridColumns": 3,
        "advfilter": "true",
        "platform": "Desktop",
        "showAdsOnNextPage": "true",
        "is_ads_enable_plp": "true",
        "displayRatings": "true"
    }

    # Send a GET request to the Ajio API for jackets
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Check if the 'products' key exists in the response data
        if 'products' in data:
            products = data['products']

            # Iterate through the list of jacket products
            for product in products:
                alt_text = product.get('images')[0].get('altText')
                brand_name = product.get('fnlColorVariantData').get('brandName')
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
                
                # Create a dictionary for each jacket product and add it to the results list
                result = {
                    "Alt Text": alt_text,
                    "Brand Name": brand_name,
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
        print(f"API request for jackets failed with status code: {response.status_code}")

    # Save the extracted jacket data to a CSV file
    with open("ajio_jackets_products.csv", "w", newline='', encoding="utf-8") as csvfile:
        fieldnames = ["Alt Text", "Brand Name", "Price (INR)", "MRP (INR)", "Discount (%)", "URL", "Image URLs"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        # Write each jacket product's data to the CSV file
        for product in results:
            writer.writerow(product)

print("Jacket data has been saved to ajio_jackets_products.csv")
