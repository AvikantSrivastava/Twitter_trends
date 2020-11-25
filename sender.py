import os
from TelegramBot import TelegramBot as BOT

def ConvertToMarkdown(Trends):
    message = "<b>Today's trends are</b> \n"

    top_counter = 10
    counter = 0
    for Trend in Trends:
        if counter < top_counter:
            message += f'<i>{Trend}</i>\n'
            continue
        elif counter == top_counter :
            message += 'Other Trends are\n'
        message += f'{Trend}, '
        counter += 1

    
    return message
        


def GetTrends():
    # Adding static trend righnow.
    # Will connect database and fetch from it later.
    Trends = ['#ThanksDrAmbedkar', '#Jallikattu', '#NivarCylone', '#ModiAgainstFarmers', '#WomenEmpowerment', 'Sanskrit', 'wooyoung', 'KIM TAEHYUNG', 'Lakshmi Vilas Bank', 'university of lucknow', 'Indian Navy', 'MS Dhoni', 'Kimmich', 'Centennial Foundation Day', 'New Zealand', 'Rape Free India', 'Tom Hagen', 'Cuddalore', 'International Day', 'adyar', 'Amit', 'BSNL', 'अहमद पटेल', '#हिंदुओं_का_हिंदुस्तान', '#AUSvINDonSony', '#DeraSachaSauda', '#SSRDishaAwaitJustice',
              '#Enemy', '#Oscars', '#OrangeTheWorld', '#ICCAwards', '#SaveAnakkayam', '#களத்தில்MKS_போஸ்டரில்EPS', '#हिन्दूओं_का_हिन्दुस्तान', '#संविधान_है_तो_भारत_है', '#GenerationEquality', '#LijoJosePellissery', '#FCGMCFC', '#കാടിനൊപ്പംകാടർക്കൊപ്പം', '#களத்தில்EPS', '#ChennaiRain', '#LaluPrasadYadav', '#SuhaneGeetWithDishTV', '#MahilaBirodhiBJP', '#Thanksgiving', '#BringMurasoliMoolapatram', '#DBSBank', '#NoHatePolitics', '#Malayalam', '#AnushkaShetty']
    return Trends

API = os.environ['TELEGRAM_BOT_API']

# Making a Telegram bot.
bot = BOT.TelegramBot(API)
ChatIDs = bot.get_ChatID()
Trends = GetTrends()

message = ConvertToMarkdown(Trends)
print([message])

bot.send(ChatIDs, message)