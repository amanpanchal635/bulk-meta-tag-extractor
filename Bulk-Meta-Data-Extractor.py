import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape meta tags from URL
def scrape_meta_tags(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title').get_text() if soup.find('title') else "N/A"
        description = soup.find('meta', attrs={'name': 'description'})
        description = description.get('content') if description else "N/A"
        return status_code, title, description
    except Exception as e:
        return "Error", "Error", str(e)

# Function to process URLs from text input
def process_urls_from_text(urls_text):
    urls_list = urls_text.split('\n')
    return urls_list

# Function to process CSV file and extract URLs
def process_urls_from_csv(uploaded_file):
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            urls_list = df.iloc[:, 0].tolist()
            return urls_list
        elif uploaded_file.name.endswith('.txt'):
            urls_list = uploaded_file.getvalue().decode("utf-8").split('\n')
            return urls_list
        else:
            return []
    else:
        return []

# Main function
def main():
    st.title("Bulk Meta Data Extractor")

        # Additional content in the sidebar
    about_section()
    support_section()

def check_url(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        status_code = response.status_code
        final_url = response.url
        return status_code, final_url
    except requests.ConnectionError:
        return "Connection Error", url

def about_section():
    st.sidebar.subheader("About")
    st.sidebar.markdown(
        "Simplify your SEO game with our Bulk Meta Title and Description Extractor Tool. Easily gather all the important meta titles and descriptions from multiple web pages at once. No more manual work or headaches—just plug in, extract, and optimize for better website visibility."
    )

def support_section():
    st.sidebar.markdown("🌟 **Support My Work!**")
    st.sidebar.markdown("Hey there, I'm [Aman Panchal](https://twitter.com/Amanpanchal0)! 👋 If you've found my work useful, consider supporting my efforts [Buy Me a ☕ Coffee](https://www.buymeacoffee.com/amanpanchal).")
    
    # Choose input method: text box or file upload
    input_method = st.radio("Choose input method:", ("Enter URLs", "Upload File"))
    
    if input_method == "Enter URLs":
        urls_text = st.text_area("Enter URLs (one per line)")
        urls_list = process_urls_from_text(urls_text)
    else:
        uploaded_file = st.file_uploader("Upload CSV or TXT file", type=['csv', 'txt'])
        urls_list = process_urls_from_csv(uploaded_file)
    
    if st.button("Extract Meta Tags"):
        if not urls_list:
            st.warning("No URLs provided.")
        else:
            data = []
            for url in urls_list:
                status_code, title, description = scrape_meta_tags(url)
                data.append((url, status_code, title, description))
            
            df = pd.DataFrame(data, columns=['URL', 'Status Code', 'Title', 'Description'])
            st.dataframe(df)
            
            if st.button("Export CSV"):
                csv_file = df.to_csv(index=False)
                st.download_button(label="Click to Download",
                                   data=csv_file,
                                   file_name="url_analysis_results.csv",
                                   mime="text/csv")
                
        # Features section
    st.subheader("Features")
    st.markdown("🔄 **Bulk Extraction:** Quickly extract meta titles and descriptions from multiple URLs simultaneously.")

    st.markdown("⚡ **Fast and Efficient:** Perform bulk extractions quickly to save time and streamline your SEO workflow.")

    st.markdown("📄 **CSV Upload:** Upload a CSV file containing a list of URLs for seamless extraction.")

    st.markdown("👀 **Preview Functionality:** Preview extracted meta titles and descriptions before exportig.")

    st.markdown("📤 **Export Options:** Export the extracted data to CSV format for further analysis or integration into other tools.")
    
if __name__ == "__main__":
    main()
