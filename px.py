import asyncio
import aiohttp

async def main():
    # target_url = "https://checkip.amazonaws.com"
    # target_url = "http://snowfl.com/"
    target_url = "https://www.youtube.com/"
    
    try:
        with open("suc1.txt", "w") as f:
            f.truncate()
        with open("err.txt", "w") as f:
            f.truncate()
    except FileNotFoundError as e:
        print(e)

    with open('prox.txt', 'r') as file:
        proxy_addresses = file.readlines()
    
    ssl_context = aiohttp.TCPConnector(ssl=False)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    async with aiohttp.ClientSession(connector=ssl_context,headers=headers) as session:
        tasks = [fetch_and_write(session,target_url,f"http://{proxyAdrs}") for proxyAdrs in proxy_addresses]
        await asyncio.gather(*tasks)

async def fetch_and_write(session, target_url, proxyAdrs):
    try:
        async with session.get(target_url, proxy=proxyAdrs) as response:
            if(response.status==200):
                with open("suc1.txt", "a") as f:
                    f.write(f"{response.status} - {proxyAdrs}\n")
    except Exception as e:
        with open("err.txt", "a") as fe:
            fe.write(f"{proxyAdrs} = {str(e)} "+'\n')

if __name__ == "__main__":
    asyncio.run(main())
