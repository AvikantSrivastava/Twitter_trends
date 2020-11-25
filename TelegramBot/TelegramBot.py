import requests
import json


class TelegramBot():
    def __init__(self, BotToken):
		# Bot Token generated from telegram
        self.Token = BotToken
        self.URL = f'https://api.telegram.org/bot{self.Token}/'

    def send(self, ChatIDs, Message):
        # Dictionary to store responses with ChatID as keys.
        responses = {}

        # Sending messages Iteratively.
        for ChatID in ChatIDs:
            Response_URL = self.URL + 'sendMessage'
            post_data = {"chat_id": ChatID, "text": Message}
            response = requests.post(Response_URL, data=post_data)
            responses[ChatID] = response
        
        # Returning HTTP Response code.
        return responses

    def get_ChatID(self):
        chatIDs = []
        data = requests.get(self.URL + 'getUpdates').json()

        for message in data['result']:
            chatID = message['message']['chat']['id']
            if chatID not in chatIDs:
                chatIDs.append(chatID)

        return chatIDs
        



