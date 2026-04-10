"""
Alicia Ganion
SDEV_220
April 4, 2026

M6_Concurrency
Part 2: Sequential
"""
import time
import requests
from bs4 import BeautifulSoup

#test URLs
urls = [
    "http://us.jellycat.com",
    "http://unicorneclipse.com",
    "http://seacroftinn.com",
    "http://hazelvillage.com",
    "http://aldeacoffee.com",
    "http://maisiepeters.co.uk"
]

#duplicate URLs for testing...that way I don't have to load in 50 websites
urls = urls * 10

#grabs the HTML content and titles
def fetch_titles(urls):
    response = requests.get(urls, timeout=5)
    soup = BeautifulSoup(response.content, 'html.parser')
    return (soup.title.string.strip()
            if soup.title else "No title available.",
            soup.get_text().strip() if soup.text else "No text available.")

#start timer
start = time.time()

#CPU-bound task -- count words on the page
def count_words(text):
    words = text.split()
    return len(words)

titles = []
word_count = []

for url in urls:
    title, html = fetch_titles(url)
    titles.append(title)
    word_count.append(count_words(html))

#end timer
end = time.time()

#print the titles with word count
for title, count in zip(titles, word_count):
    print(f"{title}: {count} words")
print(f"Runtime: {end - start}")