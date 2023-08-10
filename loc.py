# API_TOKEN = '5731462370:AAGXikaid_W3aVqNul97k0w2bbffzbMJ8Sg'
import requests
import json



BASE_URL = 'http://127.0.0.1:8000'


def create_user(username, name, user_id):
    url = f'{BASE_URL}/bot-users'
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i['user_id'] == str(user_id):
            user_exist = True
            break
    if user_exist == False:
         requests.post(url=url, data={'username':username, 'name':name, 'user_id':str(user_id)})
         return 'Create user'
  


def create_inventory(body, user_id, name):
    url = f'{BASE_URL}/inventory'
    post = requests.post(url=url, 
    data={
    'name':name,
    'body':body, 
    'user_id':user_id,
    })
    return 'Xabar yuborildi'
    print(post)

create_inventory('0080', 'text', 'name')

