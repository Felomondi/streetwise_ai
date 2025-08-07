import requests
from bs4 import BeautifulSoup

# A stable and reliable website made for practicing scraping
URL = "http://books.toscrape.com/"

def scrape_books():
    """
    Scrapes the main page of books.toscrape.com.
    """
    print("Fetching data from books.toscrape.com...")

    try:
        # Send a request to the website
        response = requests.get(URL, timeout=10)
        response.raise_for_status() # Check for any request errors

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the page title to confirm we got the right page
        page_title = soup.find('title').text
        print(f"Successfully fetched page with title: {page_title.strip()}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return False

# This allows the script to be run directly for testing
if __name__ == "__main__":
    scrape_books()