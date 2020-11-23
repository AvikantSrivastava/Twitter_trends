import requests
import json


class bot():
    def __init__(self, BotToken):

		# Bot Token generated from telegram
        self.Token = BotToken
        self.URL = f'https://api.telegram.org/bot{self.Token}/'

    def send(self, ChatID, Message):        
		Response_URL = self.URL + \
		    '/sendMessage?chat_id={{ChatID}}&parse_mode=Markdown&text={{Mesage}}'
		response = requests.get(Response_URL)
    	return response.json()




