import aiohttp
import asyncio
from bs4 import BeautifulSoup


async def main(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            resp = await response.text()
            soup = BeautifulSoup(resp, 'lxml')
            item_card = [x['href'] for x in soup.find_all('a', class_='link')]
            for url2 in item_card:
                async with session.get(url=url2) as response2:
                    resp2 = await response2.text()
                    soup2 = BeautifulSoup(resp2, 'lxml')
                    item_card2 = [x['href'] for x in soup2.find_all('a', class_='link2')]
                    for url3 in item_card2:
                        async with session.get(url=url3) as response3:
                            resp3 = await response3.text()
                            soup3 = BeautifulSoup(resp3, 'lxml')
                            item_card3 = [x['href'] for x in soup3.find_all('a', class_='link3')]
                            for url4 in item_card3:
                                async with session.get(url=url4) as response4:
                                    resp4 = await response4.text()
                                    soup4 = BeautifulSoup(resp4, 'lxml')
                                    data = [x['href'] for x in soup4.find_all('div', class_='data')]
                                    print(data)
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main('http://example.com'))