import asyncio
import aiohttp

async def main():
    # target_url = "https://checkip.amazonaws.com"
    # target_url = "http://snowfl.com/"
    target_url = "https://example.com/"
    
    with open('prox.txt', 'r') as file:
        proxy_addresses = file.readlines()
    
    # ssl_context = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession() as session:
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
