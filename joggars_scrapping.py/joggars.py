import requests
import csv

# Define the base URL of the Ajio API for Kurti and create an empty list for results
base_url = "https://www.ajio.com/api/search"
results = []

# Set the parameters for the API request for Kurti
params = {
    "fields": "SITE",
    "currentPage": 1,
    "pageSize": 40,
    "format": "json",
    "query": "kurti:relevance",
    "sortBy": "relevance",
    "text": "kurti",
    "gridColumns": 3,
    "advfilter": "true",
    "platform": "Desktop",
    "is_ads_enable_plp": "true",
    "is_ads_enable_slp": "true",
    "showAdsOnNextPage": "false",
    "displayRatings": "true",
    "segmentIds": ""
}

# Send a GET request to the Ajio API for Kurti
response = requests.get(base_url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()

    # Check if the 'products' key exists in the response data
    if 'products' in data:
        products = data['products']

        # Iterate through the list of Kurti products
        for product in products:
            brand_name = product['fnlColorVariantData']['brandName']
            price = product['price']['formattedValue']
            discount_percent = product['discountPercent']

            # Extract the image URLs
            image_urls = [image['url'] for image in product['images']]

            # Extract the product name
            product_name = product['name']

            # Create a dictionary for each Kurti product and add it to the results list
            result = {
                "Brand Name": brand_name,
                "Price (INR)": price,
                "Discount": discount_percent,
                "Product Name": product_name,
                "Image URLs": image_urls
            }
            results.append(result)

    else:
        print("Response format is not as expected")

else:
    print(f"API request for Kurti failed with status code: {response.status_code}")

# Save the extracted Kurti data to a CSV file
with open("ajio_kurti_products.csv", "w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["Brand Name", "Price (INR)", "Discount", "Product Name", "Image URLs"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Write each Kurti product's data to the CSV file
    for product in results:
        writer.writerow(product)

print("Kurti data has been saved to ajio_kurti_products.csv")
