import requests
import os
from urllib.parse import urlparse
from requests.exceptions import HTTPError
from dotenv import load_dotenv


LINK = "https://api-ssl.bitly.com/v4"


def shorten_link(headers, url: str):
    data = {"long_url": url}
    link = LINK + "/shorten"
    response = requests.post(link, headers=headers, json=data)
    response.raise_for_status()

    return response.json()['link']


def count_clicks(headers, bitlink):
    bitlink = urlparse(bitlink)
    bitlink = bitlink[1] + bitlink[2]
    params = {
        'unit': 'month',
        'units': '-1' 
        }
    link = f"{LINK}/bitlinks/{bitlink}/clicks/summary"
    response = requests.get(link, headers=headers, params=params)
    response.raise_for_status()
    
    return response.json()['total_clicks']


def is_bitlink(headers, url):
    url = urlparse(url)
    url = url[1] + url[2]
    try: 
        link = f'{LINK}/bitlinks/{url}'
        response = requests.get(link, headers=headers)
        response.raise_for_status()
        return True
    except HTTPError:
        return False


def main():
    user_url = input('Введите ссылку: ')
    token = os.environ['BITLY_TOKEN']
    headers = {
        'Authorization': f'Bearer {token}'
    }

    try:
        if is_bitlink(headers, user_url):
            sum_clik = count_clicks(headers, user_url)
            return f'По вашей ссылке прошли {sum_clik} раз(а)'
        
        return shorten_link(headers, user_url)
    except HTTPError as ex:
        return f"\n Ошибка \n\n {ex}"
    

if __name__ == '__main__':
    load_dotenv()
    print(main())
    
    