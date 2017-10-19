import socket
import telebot

API_TOKEN = '420999875:AAF91t_aa1nObHtYyd74snZKYgs3rASwGZw'

bot = telepot.TeleBot(API_TOKEN)
bot_name = "433493318"
host = socket.gethostname()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

@bot.message_handler(commands=['start'])
def check(m):
	user = bot.get_me()
	bot.send_message(m.chat.id,"hello")
	sock.bind(("192.168.0.54",7777))
	sock.listen(50)
	print("listen")
	on = None
	while True:
		on,addr = sock.accept()
		print("connect")
		bot.send_message(m.chat.id,"connect!")
		data = on.recv(1024)
		print(str(data))

start("msg")
bot.polling(none_stop=True)
