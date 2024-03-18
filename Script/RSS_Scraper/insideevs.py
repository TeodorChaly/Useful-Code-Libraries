import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json

url = "https://insideevs.com/rss/articles/all/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

articles = soup.find_all("item")
dict_info = {}
domain = ""
for article in articles:
    title = article.find("title").text
    pubdate = article.find("pubdate").text
    links = article.find_all("link")

    for link in links:
        url_parts = urlparse(link.next_sibling.strip())
        domain = url_parts.netloc
        page_link = link.next_sibling.strip()
        dict_info[page_link] = {"pubdate": pubdate, "title": title, "domain": domain}

size = 0
for page_url in dict_info:
    print(len(dict_info), "of", size)
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, "html.parser")
    try:
        class_image = soup.find(class_='originalImage scrollTieBox')
        img_tag = class_image.find("img")
        image_url = img_tag["src"]
    except:
        image_url = "No image found"
    try:
        class_content = soup.find(class_='postBody description e-content')
        content = class_content.text
        main_content = content.split(" Get the InsideEvs Newsletter S")[0]
    except:
        content = "No content found"

    dict_info[page_url]["image_url"] = image_url
    dict_info[page_url]["content"] = content
    size += 1

with open(f'{domain}_data.json', 'w', encoding="utf-8") as f:
    json.dump(dict_info, f, ensure_ascii=False, indent=4)
