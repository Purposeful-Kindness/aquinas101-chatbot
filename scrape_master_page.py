#! python

# %%

from scrapy import Spider, Request
from requests import get
from bs4 import BeautifulSoup
from pathlib import Path
import json

# %%
MASTER_PAGE_URL = "https://aquinas101.thomisticinstitute.org/saint-and-scholar"

# %%

class MasterPage(Spider):
    name = "master_page"
    
    def start_requests(self):
        urls = [
            MASTER_PAGE_URL,
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
# %%


soup = BeautifulSoup(get(MASTER_PAGE_URL).text, "html.parser")

# %%

# extract the youtube URL from the json object in soup

yt_vid = soup.find('div', class_='sqs-block-video')
# %%

yt_json = yt_vid.attrs['data-block-json']

# %%

# extract the youtube URL from the json object in soup
def extract_url_from_json(json_data):
    url_element = None
    try:
        data = json.loads(json_data)
        url_element = data.get('url')
    except json.JSONDecodeError:
        print("Invalid JSON format")

    return url_element


# %%

yt_url = extract_url_from_json(yt_json)
# %%
yt_url
# %%
