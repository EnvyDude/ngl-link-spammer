import httpx
from colorama import Fore
import os
import threading
import random



os.system('cls')
print('Enter number of threads')
threadCount = int(input(Fore.LIGHTMAGENTA_EX+"[>] "+Fore.RESET))
os.system('cls')
promxies = open('proxies.txt','r',encoding='utf-8').read().splitlines()

question = "nigga moment"

base = "https://ngl.link/api/submit"
spam = 'https://ngl.link/phantomuwunig'

successcount = 0
errors = 0

def get_device():
    mainbase = "https://www.345tool.com/api/generate/id"
    payload = '{"type":"uuid","count":1,"uuid":{"name":"","namespace":"","version":"v4","brace":false,"uppercase":false,"hyphen":true},"shortId":{"chars":"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_","length":10}}'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Length': '219',
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'www.345tool.com',
        'Origin': 'https://www.345tool.com',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Brave";v="108"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
    }
    r = httpx.post(mainbase,headers=headers,data=payload)
    if r.status_code == 201:
        code = r.text.replace('["','').replace('"]','')
        print(Fore.LIGHTGREEN_EX + '[+]Device ID : '+code + Fore.RESET)
        return code
    else:
        lines = open('deviceids.txt').read().splitlines()
        nig = random.choice(lines)
        print(Fore.LIGHTGREEN_EX + '[+]Device ID : '+ nig + Fore.RESET)
        return nig
        

headers = {
    'authority': 'ngl.link',
    'method':'POST',
    'path': '/api/submit',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://ngl.link',
    'referer': spam,
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Brave";v="108"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc':'1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

def main():
    while True:
        
        global errors
        global successcount
        proxy = random.choice(promxies)
        proxies = {
                        "http://": f"http://{proxy}",
                        "https://": f"http://{proxy}"
                    }
        name = spam.replace('https://ngl.link/','')
        deviceid = get_device()
        payload = {
    'username': name,
    'question': question,
    'deviceId': deviceid,
    'gameSlug': ''
    }
        r = httpx.post(base,headers=headers,data=payload,proxies=proxies)
        if r.status_code == 200:
            print(Fore.MAGENTA+"Request send successfully"+Fore.RESET)
            successcount += 1
            os.system('title Ngl Spammer - Success: '+str(successcount)+ ' Error: '+str(errors))
        else:
            print(Fore.RED+ "Failed to send!")
            errors += 1
            os.system('title Ngl Spammer - Success: '+str(successcount)+ ' Error: '+str(errors))

threads = []
for i in range(threadCount):
     t = threading.Thread(target=main)
     t.start()
     threads.append(t)
for i in range(threadCount):
    threads[i].join()