import requests
from bs4 import BeautifulSoup
import json

url = "https://utu.ac.id/news/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Ekstrak berita terbaru
news_title = soup.find("h4").text.strip()
news_date = soup.find("span", {"class": "date"}).text.strip()
news_content = soup.find("p").text.strip()

# Simpan ke file JSON
news_data = {
    "title": news_title,
    "date": news_date,
    "content": news_content
}

with open("latest_news.json", "w") as f:
    json.dump(news_data, f, indent=4)

print("Berita terbaru berhasil disimpan!")
