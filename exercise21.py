# Exercise 21

import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/international/"

def article_titles2txt(url_link):
    r = requests.get(url_link)
    r_html = r.text
    list_of_stories = []
    soup = BeautifulSoup(r_html, features="html5lib")
    for line in soup.find_all('h2'):
        if str(line.string) != "None" and str(line.string) != "Site Index" and str(line.string) != "Site Information Navigation":
            list_of_stories.append(line.string)
    with open('News_Stories.txt', 'w') as open_file:
        for i in list_of_stories:
            open_file.write(i+"\n")

if __name__ == "__main__":
    article_titles2txt(url)
