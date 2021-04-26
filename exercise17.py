# Exercise 17

import requests
from bs4 import BeautifulSoup
import string

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html5lib")

head_line_list = []
for head_line in soup.find_all(class_='css-xxaj7r e1lsht870'):
    head_line_list.append(head_line)


news_headings = []
for i in head_line_list:
    head_string = str(i)
    news_headings.append(head_string)

news_headings_final = []
news_headings_strip = []

for j in news_headings:
    x = j.replace("""<h3 class="css-xxaj7r e1lsht870" size="400"><span>"""," ").strip()
    news_headings_strip.append(x)

for k in news_headings_strip:
    y = k.replace("</span></h3>", " ").strip()
    news_headings_final.append(y)

for l in news_headings_final:
    print(l+"\n")
