import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json


def links_scraper(dict_info):
    data = []
    domain = "insideevs.com"

    # Load existing data from JSON file
    try:
        with open(f'{domain}_data.json', 'r', encoding="utf-8") as f:
            existing_data = json.load(f)
    except:
        existing_data = []

    # Check if the article is already in the existing data
    for page_url in dict_info:
        is_new_article = True
        for item in existing_data:
            if item["url_parts"] == page_url:
                is_new_article = False
                break

        if is_new_article:
            # If the article is new, proceed to scrape its content
            print("New article found:", page_url)
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
            except:
                content = "No content found"

            dict_info[page_url]["image_url"] = image_url
            dict_info[page_url]["content"] = content

            new_dict = {
                "domain": dict_info[page_url]["domain"],
                "url_parts": page_url,
                "date": dict_info[page_url]["pubdate"],
                "title": dict_info[page_url]["title"],
                "image_path": image_url,
                "content": content
            }
            data.append(new_dict)
            reconstruct(new_dict)

    # Add new data to the existing data
    updated_data = data + existing_data

    # Write updated data to JSON file
    with open(f'{domain}_data.json', 'w', encoding="utf-8") as f:
        json.dump(updated_data, f, ensure_ascii=False, indent=4)


def GPT_API(content):
    prompt = "Prompt: "
    print(prompt)
    return content


def reconstruct(res_dict):
    new_content = GPT_API(res_dict["content"])
    url = res_dict["url_parts"]
    domain = res_dict["domain"]
    image = res_dict["image_path"]
    date = res_dict["date"]
    data = {
        "domain": domain,
        "url_parts": url,
        "image_path": image,
        "date": date,
        "new_content": new_content
    }
    append_data_to_json([data])

def append_data_to_json(new_data):
    filename = "insideevs.com_new_data.json"
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            existing_data = json.load(f)
    except:
        existing_data = []

    existing_data.extend(new_data)

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)

def RSS_scraper():
    url = "https://insideevs.com/rss/articles/all/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = soup.find_all("item")
    dict_info = {}

    for article in articles:
        try:
            title = article.find("title").text
        except:
            title = "No title found"
        try:
            pubdate = article.find("pubdate").text
        except:
            pubdate = "No date found"
        try:
            links = article.find_all("link")

            for link in links:
                url_parts = urlparse(link.next_sibling.strip())
                domain = url_parts.netloc
                page_link = link.next_sibling.strip()
                dict_info[page_link] = {"pubdate": pubdate, "title": title, "domain": domain}
        except:
            print("No link found")

    links_scraper(dict_info)


counter = 0
while True:
    if not os.path.exists("insideevs.com_new_data.json"):
        with open("insideevs.com_new_data.json", "w") as f:
            print("File created")
    counter += 1
    RSS_scraper()
    print("Scraped", counter, "times")
    time.sleep(10)
