import requests
from bs4 import BeautifulSoup
import os

TARGET_URL = 'http://quotes.toscrape.com/page/1/' 
OUTPUT_FILENAME = 'news_headlines.txt'

def scrape_headlines(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []
    
    quote_elements = soup.find_all('span', class_='text')
    
    if not quote_elements:
        print("Could not find any elements with the specified selector.")
        return
        
    for element in quote_elements:
        headlines.append(element.get_text(strip=True))

    if headlines:
        print(f"Found {len(headlines)} items. Saving to {OUTPUT_FILENAME}")
        try:
            with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
                for headline in headlines:
                    f.write(headline + '\n')
            
            print(f"Success! Headlines saved to: {os.path.abspath(OUTPUT_FILENAME)}")
            
        except IOError as e:
            print(f"Error writing to file: {e}")
    else:
        print("No headlines were scraped to save.")

if __name__ == "__main__":
    scrape_headlines(TARGET_URL)