import sys
from bs4 import BeautifulSoup
import requests

url = "http://nytimes.com/"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")
titles = soup.find_all("article")
for heading in titles:
    print(heading.h2.text.strip())
sys.exit()