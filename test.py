import requests
import concurrent.futures

def check_proxy_responses(proxy_addresses, target_url):
    for proxy_address in proxy_addresses:
        proxy_address = proxy_address.strip()
        check_proxy_response(proxy_address, target_url)

def check_proxy_response(proxy_address, target_url):
    proxies = {
        'http': f'http://{proxy_address}',
        'https': f'http://{proxy_address}'
    }

    try:
        response = requests.get(target_url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            with open('suc1.txt', 'a') as f:
                f.write(proxy_address + '\n') 
            # print(proxy_address+ " = "+response.text)
    except requests.exceptions.RequestException as e:
        with open('err.txt', 'a') as f:
            f.write(str(e)+'\n')

def main():
    target_url = "https://checkip.amazonaws.com"
    # target_url = "http://snowfl.com/"
    chunk_size = 50
    
    with open('prox.txt', 'r') as file:
        proxy_addresses = file.readlines()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for i in range(0, len(proxy_addresses), chunk_size):
            chunk = proxy_addresses[i:i+chunk_size]
            executor.submit(check_proxy_responses, chunk, target_url)

if __name__ == "__main__":
    main()
