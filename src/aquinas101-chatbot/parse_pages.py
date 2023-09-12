#! python

from requests import get
from bs4 import BeautifulSoup
import json


def extract_url_from_json(json_data):
    url_element = None
    try:
        data = json.loads(json_data)
        url_element = data.get("url")
    except json.JSONDecodeError:
        print("Invalid JSON format")

    return url_element


# write a function to take a str URL and retrieve the document
def get_page(url):
    return get(url).text


# write a functiont to take the document and return a BeautifulSoup object
def get_soup(page):
    return BeautifulSoup(page, "html.parser")


# write a function to take the soup and return the youtube URL
def get_youtube_url(soup):
    yt_vid = soup.find("div", class_="sqs-block-video")
    yt_json = yt_vid.attrs["data-block-json"]
    return extract_url_from_json(yt_json)


# write a function to extract URLs from the soup that match the domain pattern
def get_urls(soup, domain_pattern):
    urls = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and domain_pattern in href:
            urls.append(href)
    return urls
