import nexmo
from envparse import env

env.read_envfile()

client = nexmo.Client(key=env('API_KEY'), secret=env('API_SECRET'))

number = input('Enter the number')

message = input('Enter the message')

response = client.send_message({'from': 'Nexmo', 'to': number, 'text': message})

response = response['messages'][0]

if response['status'] == '0':
    print('Sent message', response['message-id'])
else:
    print('Error')
