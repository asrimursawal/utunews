import requests
from bs4 import BeautifulSoup
import json

# URL website UTU bagian berita
url = "https://utu.ac.id/news/"

# Fungsi untuk mengambil berita terbaru
def fetch_latest_news():
    try:
        # Kirim permintaan ke website UTU
        response = requests.get(url)
        response.raise_for_status()  # Pastikan permintaan berhasil

        # Parsing HTML dengan BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Temukan elemen berita terbaru
        news_title = soup.find("h4").text.strip()  # Judul berita
        news_date = soup.find("span", {"class": "date"}).text.strip()  # Tanggal berita
        news_content = soup.find("p").text.strip()  # Isi singkat berita

        # Struktur data berita
        news_data = {
            "title": news_title,
            "date": news_date,
            "content": news_content
        }

        # Simpan data ke file JSON
        with open("latest_news.json", "w") as f:
            json.dump(news_data, f, indent=4)

        print("Berita terbaru berhasil disimpan!")

    except Exception as e:
        print(f"Gagal mengambil berita: {e}")

# Jalankan fungsi
if __name__ == "__main__":
    fetch_latest_news()
