# Streamlit Bulk URL Metadata Extractor

## Overview

This is a simple web application built with [Streamlit](https://streamlit.io/) that allows users to input a list of URLs from a website. The program analyzes each URL and extracts the meta title and meta description, storing this information in a Pandas dataframe. It also checks the status code of each URL request and records the status code in the dataframe.

## Features

- Manually enter URLs or upload a CSV/TXT file containing URLs.
- Extract metadata including meta title, meta description, and status code for each URL.
- Export metadata to a CSV file for further analysis.

## Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/amanpanchal635/bulk-meta-tag-extractor.git
```

2. Install the required dependencies by running:

```bash
cd bulk-meta-tag-extractor
pip install -r requirements.txt
```

3. Run the Streamlit app using the following command:

```bash
streamlit run app.py
```

## Usage

1. Choose the method to input URLs: manually enter URLs or upload a CSV/TXT file containing URLs.
2. Click on "Extract Metadata" to analyze the URLs and display the metadata in a table.
3. Optionally, export the metadata to a CSV file by clicking on "Export to CSV".

## Dependencies

- streamlit==1.6.0
- pandas==1.3.3
- requests==2.26.0
- beautifulsoup4==4.10.0

## Screenshots

![Screenshot 2024-02-15 200500](https://github.com/amanpanchal635/bulk-meta-tag-extractor/assets/141056736/9bbcf2fa-838a-48eb-aae3-7fd1ac24f3d3)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
