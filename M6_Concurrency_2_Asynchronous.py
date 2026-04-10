"""
Alicia Ganion
SDEV_220
April 9, 2026

M6_Concurrency
Part 2: Asynchronous I/O
"""
import time
import requests
import aiohttp
import asyncio
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

#grabs the title from the test URLs
async def fetch_data(session, url):
    #stops after 5 seconds if site is unreachable
    response = await session.get(url, timeout=5)
    html = await response.read()
    #this turns HTML into something searchable
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string.strip() if soup.title else "No title available."
    text = soup.text.strip() if soup.text else "No text available."
    return title, text

#computer bound task
def count_words(text):
    words = text.split()
    return len(words)

#event loop with async
async def main():
    async with aiohttp.ClientSession() as session:
        #create tasks for all URLs
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    #this is the cpu work sequentially
        final_results = []
        for title, text in results:
            word_count = count_words(text)
            final_results.append([title, word_count])
        return final_results

#start timer
start = time.time()

#run the program
if __name__ == "__main__":
    results = asyncio.run(main())

#end timer
end = time.time()

for title, count in results:
    print(f"{title}: {count} words")

print("Total Runtime: ", end - start)