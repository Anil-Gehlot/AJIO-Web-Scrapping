import requests
import csv

# Define the base URL of the Ajio API and create an empty list for results
base_url = "https://www.ajio.com/api/category/83"
results = []

for page in range(500):

    # Set the parameters for the API request for jeans
    params = {
        "currentPage": page,  # Specify the desired page number
        "pageSize": 40,
        "format": "json",
        "query": ":relevance:curated:true:curatedId:jeans-3571-88891:head:Jeans",
        "sortBy": "relevance",
        "curated": "true",
        "gridColumns": 3,
        "advfilter": "true",
        "platform": "Desktop",
        "showAdsOnNextPage": "true",
        "is_ads_enable_plp": "true",
        "displayRatings": "true"
    }

    # Send a GET request to the Ajio API for jeans
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Check if the 'products' key exists in the response data
        if 'products' in data:
            products = data['products']

            # Iterate through the list of jeans products
            for product in products:
                alt_text = product.get('images')[0].get('altText')
                brand_name = product.get('fnlColorVariantData').get('brandName')
                price = product.get('price').get('formattedValue')
                discount_percent = product.get('discountPercent')
                
                # Extract the image URLs
                image_urls = [image['url'] for image in product.get('images')]
                
                url = "https://www.ajio.com" + product.get('url')
                
                # Create a dictionary for each jeans product and add it to the results list
                result = {
                    "Alt Text": alt_text,
                    "Brand Name": brand_name,
                    "Price (INR)": price,
                    "Discount": discount_percent,
                    "URL": url,
                    "Image URLs": image_urls
                }
                results.append(result)

        else:
            print("Response format is not as expected")

    else:
        print(f"API request for jeans failed with status code: {response.status_code}")

    # Save the extracted jeans data to a CSV file
    with open("ajio_jeans_products.csv", "w", newline='', encoding="utf-8") as csvfile:
        fieldnames = ["Alt Text", "Brand Name", "Price (INR)", "Discount", "URL", "Image URLs"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        # Write each jeans product's data to the CSV file
        for product in results:
            writer.writerow(product)

print("Jeans data has been saved to ajio_jeans_products.csv")
