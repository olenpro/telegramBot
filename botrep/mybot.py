import telebot
#1660344529:AAFxYzr0ddrLlaWiRvm8zXiVmWa35csYvws
#testHelgBot
#test_helgpro_bot
bot = telebot.TeleBot("1660344529:AAFxYzr0ddrLlaWiRvm8zXiVmWa35csYvws")

#Обработчик команд
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
#Обработчик событий
@bot . message_handler ( func = lambda  m :  True ) 
def  echo_all ( message ): 
	if message.text=='Привет':
		bot . reply_to (message, "О здороу")
	elif  message.text=='Как':
		bot . reply_to (message, " Норм все")
	elif  message.text=='хрень':
		bot . reply_to (message, " И не говори")

bot.polling()