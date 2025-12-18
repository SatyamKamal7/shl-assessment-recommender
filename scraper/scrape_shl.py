import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.shl.com/solutions/products/"

def scrape_shl():
    response = requests.get(URL, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    data = []
    for card in soup.select(".product-card"):
        data.append({
            "assessment_name": card.get_text(strip=True),
            "description": card.get_text(strip=True),
            "url": URL
        })

    with open("data/shl_catalogue.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    scrape_shl()