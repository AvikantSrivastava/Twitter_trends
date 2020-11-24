import os
from TelegramBot import TelegramBot

# initializing bot with API key
tweet_bot = TelegramBot(os.environ['TELEGRAM_BOT_API'])

# Get Chat ID from telegram subscribers
ChatIDs = tweet_bot.get_ChatID()

# Sending ChatIDs and message 
tweet_bot.send(ChatIDs, 'Hey buddy sup?')

print(ChatIDs)