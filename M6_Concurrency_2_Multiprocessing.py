"""
Alicia Ganion
SDEV_220
April 9, 2026

M6_Concurrency
Part 2: Multiprocessing
"""
import time
from concurrent.futures import ThreadPoolExecutor
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

#grabs the titles and text
def fetch_titles(urls):
    response = requests.get(urls, timeout=5)
    soup = BeautifulSoup(response.content, 'html.parser')
    return (soup.title.string.strip()
            if soup.title else "No title available.",
            soup.get_text().strip() if soup.text else "No text available.")
#grabs the titles and text
def fetch_titles(urls):
    response = requests.get(urls, timeout=5)
    soup = BeautifulSoup(response.content, 'html.parser')
    return (soup.title.string.strip()
            if soup.title else "No title available.",
            soup.get_text().strip() if soup.text else "No text available.")

#CPU task
def count_words(text):
    words = text.split()
    return len(words)

#combines def fetch_titles and def count_words
def process_tasks(urls):
    title, text = fetch_titles(urls)
    word_count = count_words(text)
    return title, word_count

#start up the timer
start = time.time()

#multiprocessing starts
if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(process_tasks, urls))

#end the timer
end = time.time()

#print the results
for title, count in results:
    print(f"{title}: {count} words")
print(f"Total runtime: {end - start}")