import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
print(f"--- Visiting {url} ---")

try:
    # 1. Get the page
    r = requests.get(url)
    # 2. Parse the code
    soup = BeautifulSoup(r.text, 'html.parser')
    # 3. Find the first 3 headlines
    lines = soup.find_all('span', class_='titleline', limit=3)

    print("\nSUCCESS! Here is the news:")
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line.text}")

except Exception as e:
    print(f"Connection failed: {e}")


