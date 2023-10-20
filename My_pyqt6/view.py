import json
import aiohttp
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}


async def async_request(url: str, headers: dict) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as response:
            data = await response.read() # is bytes
            return data.decode("utf-8") # decode to str

async def get_news(url: str) -> str:
    news = await async_request(url=url, headers=headers)
    news = json.loads(news)['news']
    txt1 = ""
    for i in news:
        txt1 += f"({i['id']}){i['title']}\n"
        for j in range(5):
            txt1 += f"({i['id']}){i['title']}\n"

    return txt1

