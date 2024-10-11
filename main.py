import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6986373519:AAGkd_dmH4JdMhtjOfm75CuyBmDvSiBMfJQ'
TEXT = 'Опа, апдейт'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int
get_text = ''

while True:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            get_text = result['message']['text']
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    if get_text.upper() == 'STOP':
        break
    time.sleep(1)
    counter += 1
