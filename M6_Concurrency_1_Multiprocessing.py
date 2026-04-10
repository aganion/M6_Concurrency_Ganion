"""
Alicia Ganion
SDEV_220
April 4, 2026

M6_Concurrency
Part 1: Multiprocessing
"""
import time
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

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

#grabs the title from the test URLs
def fetch_title(url):
    #stops after 5 seconds if site is unreachable
    response = requests.get(url, timeout=5)
    #this turns HTML into something searchable
    soup = BeautifulSoup(response.content, "html.parser")
    #find <title> tag and grabs text string from inside
    return soup.title.string.strip() if soup.title else "No title available."

#start timer
start = time.time()

if __name__ == "__main__":

    with ThreadPoolExecutor(max_workers=10) as executor:
        titles = list(executor.map(fetch_title, urls))

#end timer
end = time.time()

print("Multiprocessing titles: ", titles)
print("Total Runtime: ", end - start)
