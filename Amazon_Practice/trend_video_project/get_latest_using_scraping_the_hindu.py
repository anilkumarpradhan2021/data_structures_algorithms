import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import random
import time
from PIL import Image
from io import BytesIO

# Function to fetch the latest news dynamically with more content, including images (absolute URLs)
def fetch_latest_news_from_scraping(url):
    # List of user-agent strings to simulate different browsers
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; rv:40.0) Gecko/20100101 Firefox/40.0"
    ]

    headers = {
        "User-Agent": random.choice(user_agents)  # Randomize User-Agent for each request
    }
    
    try:
        # Send the GET request for the main page
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return
        
        # Parse the content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Try finding common tags for headlines (h1, h2, h3, etc.)
        headline_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        articles = []

        # Loop through common headline tags and find articles
        for tag in headline_tags:
            for element in soup.find_all(tag):
                headline = element.get_text(strip=True)
                print(f"Headlines : {headline}")
                if headline:  # Ensure it's not empty
                    article = {"title": headline}

                    # Try to find the description (e.g., <p> or <meta name="description">)
                    description = None
                    description_tag = element.find_next('p')  # Find next <p> tag after headline
                    if description_tag:
                        description = description_tag.get_text(strip=True)

                    # Find the URL (if the headline is a link)
                    article_link = element.find_next('a', href=True)
                    if article_link:
                        article["url"] = urljoin(url, article_link['href'])  # Make URL absolute
                    else:
                        # If no link is found in the headline, we use the main URL as fallback
                        article["url"] = url

                    # Add the description if available
                    article["description"] = description if description else "No description available."

                    # Try to find images related to the article
                    images = get_images_from_article(soup, article["url"])
                    article["urlToImage"] = images if images else None
                    
                    # Add the article to the list
                    articles.append(article)

        # If no articles were found in common tags, try searching <a> tags for news links
        if not articles:
            print("No headlines found in header tags. Searching <a> tags...")
            for a in soup.find_all('a', href=True):
                text = a.get_text(strip=True)
                if text and len(text.split()) > 3:  # Check for longer text to avoid short links
                    article = {"title": text, "url": urljoin(url, a['href']), "description": "No description available.", "urlToImage": None}
                    articles.append(article)

        # Visit each article and scrape images from them
        for article in articles[1:2]:
            article_url = article['url']
            print(f"\nVisiting: {article_url}")
            article['urlToImage'] = fetch_images_from_article(article_url, headers)

        # Display results (only first 10 articles)
        if articles:
            print("\nLatest News Headlines and More Content:")
            for i, article in enumerate(articles[1:2]):  # Display top 2 articles
                print(f"{i+1}. {article['title']}")
                print(f"   URL: {article['url']}")
                print(f"   Description: {article['description']}")
                print(f"   Image URLs: {', '.join(article['urlToImage'])}")
                print("-" * 50)
        else:
            print("No articles found.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
    
    return articles


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from PIL import Image
from io import BytesIO

def fetch_images_from_article(article_url, headers):
    images = set()  # Use a set to ensure uniqueness
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg']  # List of valid image extensions
    image_sizes = {}  # Dictionary to store images and their sizes (width * height)

    try:
        # Send a GET request to the article URL
        response = requests.get(article_url, headers=headers)
        if response.status_code == 200:
            article_soup = BeautifulSoup(response.text, 'html.parser')

            # Try to find the main content section
            article_section = article_soup.find('article') or article_soup.find('main') or article_soup.find('section')
            if not article_section:
                # If no article or main section found, just consider the body
                article_section = article_soup.find('body')

            # Find all <img> tags within the main article section
            for img_tag in article_section.find_all('img', src=True):
                src = img_tag.get('src')
                if not src:
                    continue

                # Check if the image URL has a valid image extension
                if any(src.lower().endswith(ext) for ext in valid_extensions):
                    # Resolve relative image URLs to absolute URLs
                    img_url = urljoin(article_url, src)

                    # Check if image is part of the main article content (ignore images in header/footer/sidebar)
                    if 'header' in img_tag.get('class', []) or 'footer' in img_tag.get('class', []):
                        continue

                    # Fetch the image content to get its dimensions
                    try:
                        img_response = requests.get(img_url, headers=headers)
                        if img_response.status_code == 200:
                            img = Image.open(BytesIO(img_response.content))

                            # Get the image dimensions (width and height)
                            img_width, img_height = img.size  # (width, height)

                            # Calculate the area (width * height) and store the image size
                            if img_width > 0 and img_height > 0:
                                image_size = img_width * img_height
                                image_sizes[img_url] = image_size  # Store image URL with its size

                    except Exception as e:
                        print(f"Error fetching image {img_url}: {e}")
                        continue

            # Now, find the maximum size image(s)
            if image_sizes:
                max_size = max(image_sizes.values())
                # Filter images that have the maximum size
                for img_url, size in image_sizes.items():
                    if size == max_size:
                        images.add(img_url)  # Add to set (unique URLs)

        else:
            return ["Error fetching article images."]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the article: {e}")
        return ["Error fetching article images."]
    
    # Convert the set to a list to return as the result
    return list(images)

import re

def convert_to_numeric(input_string):
    # Ensure input is a string
    input_string = str(input_string)

    # Remove all non-numeric characters (including commas, periods, etc.)
    cleaned_string = re.sub(r'[^0-9.]', '', input_string)

    # Convert to numeric type (float or int depending on the presence of a decimal point)
    if '.' in cleaned_string:
        return float(cleaned_string)  # Convert to float if a decimal point is present
    else:
        return int(cleaned_string)    # Convert to int if no decimal point


# Function to find images from the main page of news site
def get_images_from_article(soup, base_url):
    print(f"Navigate to ---- {base_url}")
    images = []
    # Try to find images in the main page (usually first <img> or hero image)
    for img_tag in soup.find_all('img'):
        src = img_tag.get('src')
        if src:
            img_url = urljoin(base_url, src)
            
            # Add image URL to the list if it's large enough
            img_width = convert_to_numeric(img_tag.get('width', 200))
            img_height = convert_to_numeric(img_tag.get('height', 200))
                        
            if img_width and img_height:
                img_width = int(float(img_width))
                img_height = int(float(img_height))
                if img_width > 100 and img_height > 100:  # Filter out tiny images (e.g., thumbnails)
                    images.append(img_url)

    return images

# Example Usage
url = "https://www.ndtv.com/"
fetch_latest_news_from_scraping(url)

# Adding delay to avoid overloading the server with requests
time.sleep(random.randint(1, 3))  # Random sleep time between requests (to prevent rate-limiting)
