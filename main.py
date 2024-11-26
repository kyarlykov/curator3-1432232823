from telebot import TeleBot
bot = TeleBot('7749241614:AAEfXXpWp9xo8YDwLPqHPgrRV_YCgnQDVgY')

@bot.message_handler(commands=['start'])
def start(message):
      bot.send_message(message.chat.id, 'Привет, я Питоша,я твой гороскоп печенек ', parse_mode='Markdown')
        
@bot.message_handler(commands=['today'])
def today(message):
      bot.send_message(message.chat.id,'[*Печенька сегодняшнего дня*](https://www.scarlett.ru/upload/resize_cache/webp/iblock/605/77nrxyach9w191dubxh8ooe2st5zhzvn/960_5000_1/domashnee_pechene_top_20_receptov_1.webp) ', parse_mode='Markdown')
        
@bot.message_handler(commands=['tomorrow'])
def tomorrow(message):
      bot.send_message(message.chat.id,'[*Печеька завтрашнего дня*](https://img.iamcook.ru/2022/upl/recipes/zen/u-9bbf3c0a8b324a3cd5e7d184e4778950.JPG) ', parse_mode='Markdown')
        
bot.infinity_polling()