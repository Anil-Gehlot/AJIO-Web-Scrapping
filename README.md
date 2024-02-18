# AJIO Web Scraping

Welcome to the AJIO Web Scraping repository! This repository contains a web scraper for the Ajio website, designed to extract data for analysis and research purposes. The scraper is written in Python programming language.

## Overview

The web scraper in this repository is tailored specifically for extracting data from various categories of products on the Ajio website. Each category has its own Python script for scraping data and a corresponding CSV file containing the scraped data.

## Repository Structure

The repository is organized into folders, each representing a different category of products. Each folder contains a Python script for scraping data from that category and a CSV file containing the scraped data. Here's an overview of the structure:

- `boot_scrapping.py`: Python script for scraping data related to boots.
- `heels_scrapping.py`: Python script for scraping data related to heels.
- `jacket_scrapping.py`: Python script for scraping data related to jackets.
- `jeans_scrapping.py`: Python script for scraping data related to jeans.
- `joggars_scrapping.py`: Python script for scraping data related to joggers.
- `kurti_scrapping.py`: Python script for scraping data related to kurtis.
- `shirt_scrapping.py`: Python script for scraping data related to shirts.
- `shoes_scrapping.py`: Python script for scraping data related to shoes.
- `top_scrapping.py`: Python script for scraping data related to tops.

Each of the above scripts is responsible for scraping data for its respective category and saving it to a CSV file in the same folder.

## Usage

To use the web scraper:

1. Navigate to the folder corresponding to the category you want to scrape.
2. Run the Python script (`*.py`) using a Python interpreter.
3. The script will scrape data from the respective category on the Ajio website and save it to the corresponding CSV file (`*.csv`) in the same folder.

## Dependencies

The scraper requires the following dependencies:

- Python 3.x
- Beautiful Soup
- Requests library

You can install the dependencies using pip:

```bash
pip install beautifulsoup4 requests
```

## Support
If you encounter any issues with the scraper or have any questions, please feel free to open an issue. Your feedback and contributions are highly appreciated!

Happy scraping! 🕸️
