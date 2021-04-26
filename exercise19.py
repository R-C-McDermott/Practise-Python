# Exercise 19

import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"


def print_html_article_story(url_link):
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, features="html5lib")
    for line in soup.find_all('p'): # finds all <p> tags
        if str(line.string) != "None": # lines without <p> tag appear as "None"... this line removes them
            print(line.string)

if __name__ == "__main__":
    print_html_article_story(url)
