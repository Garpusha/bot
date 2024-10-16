from asyncio import timeout

import requests
# from pprint import pprint
import time

with open('http_api_token.txt', 'r') as token_file:
    BOT_TOKEN = token_file.readline()

API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'

ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('

offset = -2
counter = 0
time_out = 50
cat_response: requests.Response
cat_link: str


while True:
    # print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={time_out}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
                print(f"A cat was sent to user {result['message']['from']['first_name']}")
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    # counter += 1