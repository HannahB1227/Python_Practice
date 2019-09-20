import sys
from bs4 import BeautifulSoup
import requests

url = "http://nytimes.com/"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")
titles = soup.find_all("article")
filename = input("Enter file name and type: ")
with open(filename, 'w') as open_file:
    for heading in titles:
        open_file.write(heading.h2.text.strip() + "\n")
sys.exit()