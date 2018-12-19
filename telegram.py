import time, datetime #time access
import telepot 
import os # operating system interface
import sys #system specific parameters and function
from telepot.loop import MessageLoop #receive message from client
from pprint import pprint
now = datetime.datetime.now()

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    print ("Received: %s" % command)

    if command == '/start':
        telegram_bot.sendMessage (chat_id, str("menu : /hi /time /logo /file /audio"))
        response = telegram_bot.getUpdates(msg)
        print (pprint(response))
    
    elif command == '/hi':
        telegram_bot.sendMessage (chat_id, str("Hi! Muhammad Syafiq"))
        

    elif command == '/time':
        telegram_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))

    elif command == '/logo':
        telegram_bot.sendPhoto(chat_id, photo= open('/home/pi/myprojects/pi3.jpeg',"rb"))

    elif command == '/file':
        telegram_bot.sendDocument(chat_id, document=open('/home/pi/myprojects/telegram.py'))
        
    elif command == '/audio':
        telegram_bot.sendAudio(chat_id, audio=open('/home/pi/myprojects/alarm.wav',"rb"))
    
        
telegram_bot = telepot.Bot('PUT YOUR TOKEN HERE') 
print (telegram_bot.getMe()) #token telegram bot api

MessageLoop(telegram_bot, action).run_as_thread()
print ("Up and Running....")

#store data in file
f=open('/home/pi/myprojects/logfile.txt',"a")
time_connect = "time connected :" + str(now.hour)+str(":")+str(now.minute)
print(time_connect)
f.write(time_connect)
f.write("\n")
f.close()

while 1:
    time.sleep(10)
