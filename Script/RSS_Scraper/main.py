from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

url = "https://insideevs.com/rss/articles/all/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

articles = soup.find_all("item")

for article in articles:
    title = article.find("title").text
    pubdate = article.find("pubdate").text
    links = article.find_all("link")
    print("---")
    print(title)
    print(pubdate)
    for link in links:
        url_parts = urlparse(link.next_sibling.strip())
        domain = url_parts.netloc
        print(link.next_sibling.strip())
        print(domain)

