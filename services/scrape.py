import requests
from bs4 import BeautifulSoup



def fetch_webpage_content(url: str) -> str:
    print(f"Crawling URL {url}")
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    body = soup.find('body')
    content = ""
    if body:
        content = body.get_text(separator='\n', strip=True)  # Get all text within the <body>, separated by newlines


    return content
