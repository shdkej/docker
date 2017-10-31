import socket
import telebot
import subprocess
import logging
from telebot import types

API_TOKEN = '420999875:AAF91t_aa1nObHtYyd74snZKYgs3rASwGZw'

bot = telebot.TeleBot(API_TOKEN)
bot_name = "433493318"
host = socket.gethostname()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#itembtn1 = types.KeyboardButton('/test')
markup.row('/vmstat','/tomcat')

@bot.message_handler(commands=['start'])
def check(m):
	user = bot.get_me()
	bot.send_message(m.chat.id,"hello",reply_markup=markup)
	logging.info("listen")
	on = None
	while True:
		on,addr = sock.accept()
		logging.info("connect")
		bot.send_message(m.chat.id,"connect!")
		data = on.recv(1024)
		strdata = str(data)
		print(strdata)
		bot.send_message(m.chat.id,strdata)
	on.close()

def finish():
	bot.send_message(bot_name,"SERVER DOWN!")

@bot.message_handler(commands=['server'])
def serverOn(m):
	message = "on"
	bot.send_message(m.chat.id,message)

@bot.message_handler(commands=['vmstat','tomcat'])
def serverSystem(m):
	result = ""
	if m.text == '/vmstat' :
		result = subprocess.check_output('vmstat',shell=True)
	if m.text == '/tomcat' :
		command = "docker exec tomcat cat logs/localhost_access_log.$(date '+%Y-%m-%d').txt | grep /board | tail"
		result = subprocess.check_output(command,shell=True) 
	bot.send_message(m.chat.id,result)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	msg = "you said : "+message.text
	bot.reply_to(message,msg)

#def tomcat_monitor():
#	command = "docker exec tomcat find logs/ -mmin -10"
#	tomcatcommand = "docker exec tomcat cat logs/localhost_access_log.$(date '+%Y-%m-%d').txt | grep /board | tail"
#	while True:
#		result = subprocess.check_output(command,shell=True)
#		tomcat = subprocess.check_output(tomcatcommand,shell=True)
#		if result is not None:
#			bot.send_message(bot_name,tomcat)

if __name__ == '__main__':
	sock.bind(("59.27.177.110",7777))
	sock.listen(50)
	logging.getLogger().setLevel(logging.DEBUG)
	logging.info("SERVER START")
	bot.polling()
#	tomcat_monitor()

finish()
