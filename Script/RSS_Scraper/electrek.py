from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import json

url = "https://electrek.co/feed/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
items = soup.find_all("item")

data = []

domain_name = "electrek.co"
counter = 0
for item in items:
    print(len(items) - counter)

    title = item.find("title").text
    links = item.find("link")
    url_parts = links.next_sibling.strip()
    domain = url_parts.split(".co")[0] + ".co"

    response = requests.get(url_parts)
    soup = BeautifulSoup(response.content, "html.parser")
    date = soup.find(class_="author-name").next_sibling[2:]
    content = soup.find(class_="container med post-content").text
    image = soup.find(class_="img-border featured-image")
    try:
        image_path = image.find("img")["src"]
    except:
        print(url_parts)

        image_path = "No image found"

    article_data = {
        "domain": domain,
        "url_parts": url_parts,
        "date": date,
        "title": title,
        "image_path": image_path,
        "content": content
    }

    data.append(article_data)
    counter += 1
    if counter == 5:
        break

with open(f'{domain_name}_data.json', 'w', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
