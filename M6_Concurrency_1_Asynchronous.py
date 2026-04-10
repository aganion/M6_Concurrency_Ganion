"""
Alicia Ganion
SDEV_220
April 4, 2026

M6_Concurrency
Part 1: Asynchronous I/O
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
async def fetch_title(session, url):
    #stops after 5 seconds if site is unreachable
    response = await session.get(url, timeout=5)
    html = await response.read()
    #this turns HTML into something searchable
    soup = BeautifulSoup(html, "html.parser")
    #find <title> tag and grabs text string from inside
    return soup.title.string.strip() if soup.title else "No title available."

#event loop with async
async def main():
    async with aiohttp.ClientSession() as session:
        #create tasks for all URLs
        tasks = [fetch_title(session, url) for url in urls]
        titles = await asyncio.gather(*tasks)
        return titles

#start timer
start = time.time()

#run the event loop
if __name__ == "__main__":
    titles = asyncio.run(main())
#end timer
end = time.time()
print("Asynchronous I/O titles: ", titles)
print("Total Runtime: ", end - start)