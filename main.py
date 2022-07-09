import requests
import json
import math



cookies = {
#Will add auto cookies, useyour own
}

headers = {
    'authority': 'stockx.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'app-platform': 'Iron',
    'app-version': '2022.07.03.02',
    'authorization': '#authcookie'
    'cache-control': 'no-cache',
    'dnt': '1',
    'pragma': 'no-cache',
    'referer': 'https://stockx.com',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

vparams = {
    'limit': '50',
    'page': '1',
    'sort': 'createdAt',
    'order': 'DESC',
    'state': '480',
    'currency': 'USD',
    'country': 'US',
}

def get_info():
    searchvalue = input('Search Query:\n')
    sparams = {
    '_search': searchvalue,
    }
    print()
    sitem = requests.get('https://stockx.com/api/browse', params=sparams, cookies=cookies, headers=headers)
    s1 = sitem.json()
    dataid = s1['Products'][0]['uuid']
    title = s1['Products'][0]['title']
    response = requests.get(f'https://stockx.com/api/products/{dataid}/activity', params=vparams, cookies=cookies, headers=headers)
    r1 = response.json()

    for i in range (0,30): #last 30 sales
        price = r1['ProductActivity'][i]['amount']
        date = r1['ProductActivity'][i]['createdAt']
        size = r1['ProductActivity'][i]['shoeSize']
        print(f'Price => {(math.ceil(price))} | Date => {date} | Size {size} - {title}')
        
        
get_info()
