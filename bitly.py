import requests
import os
from requests.exceptions import HTTPError, ConnectionError
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN')
LINK = "https://api-ssl.bitly.com/v4"
user_url = input('Введите ссылку: ')


def get_headers(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    return headers



def chek_response(url: str):
    if not("http" in url):
        url = f'https://{url}'

    response = requests.get(url)
    response.raise_for_status()
        


def format_for_bitlink(url: str):
    if url.startswith("https://"):
        url = url.replace('https://', '')
        return url
    
    return url



def shorten_link(token, url: str):
    if not(url.startswith("https://")) and not(url.startswith("http://")):
        url = f'https://{url}'

    data = f'{{ "long_url": "{url}"}}'
    link = LINK + "/shorten"
    response = requests.post(link, headers=get_headers(token), data=data)
    response.raise_for_status()
    bitlink = response.json()['link']
    chek_response(bitlink)

    return bitlink



def count_clicks(bitlink: str):
    bitlink = format_for_bitlink(bitlink)
    params = {
        'unit': 'month',
        'units': '-1' 
        }
    link = f"{LINK}/bitlinks/{bitlink}/clicks/summary"
    response = requests.get(link, headers=get_headers(TOKEN), params=params)
    response.raise_for_status()
    summ = response.json()['total_clicks']
    
    return f'По вашей ссылке прошли: {summ} раз(а)'



def is_bitlink(url: str):
    try:
        try:
            chek_response(url)
        except (HTTPError, ConnectionError) as ex:
            return "Вы ввели что-то не корректное"

        url = format_for_bitlink(url)
        link = f'{LINK}/bitlinks/{url}'
        response = requests.get(link, headers=get_headers(TOKEN))
        response.raise_for_status()
        return True
    except HTTPError:
        return False



def main():
    try:
        if is_bitlink(user_url):
            return count_clicks(user_url)
        return shorten_link(TOKEN, user_url)
    except HTTPError as ex:
        return f"Ошибка \n\n {ex}"
    


if __name__ == '__main__':
    print(main())
    
    