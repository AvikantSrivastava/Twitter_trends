import requests
import json


class TelegramBot():
    def __init__(self, BotToken):
		# Bot Token generated from telegram
        self.Token = BotToken
        self.URL = f'https://api.telegram.org/bot{self.Token}/'

    def send(self, ChatIDs, Message):

        responses = {}

        for ChatID in ChatIDs:
            Response_URL = self.URL + f'sendMessage?chat_id={ChatID}&parse_mode=Markdown&text={Message}'
            print(Response_URL)
            responses[ChatID] = requests.get(Response_URL)
        return responses

    def get_ChatID(self):
        chatIDs = []
        data = requests.get(self.URL + 'getUpdates').json()

        for message in data['result']:
            chatID = message['message']['chat']['id']
            if chatID not in chatIDs:
                chatIDs.append(chatID)

        return chatIDs
        



