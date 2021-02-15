import telebot
import time
import mysql.connector
from msges import *

token = '1381385019:AAFJpXE-5rURhddCSVYrEGss2Kv-EYrJwUQ'
dobby = telebot.TeleBot(token = token)

def getLang(dict, str):
    for key in dict:
        if dict[key] == str:
            return key

@dobby.message_handler(commands = ['start', 'փոխել_լեզուն', 'change_language', 'изменить_язык'])
def startChat(message):    
    menuLang = [[telegram.KeyboardButton('/Հայերեն')], [telegram.KeyboardButton('/English')], [telegram.KeyboardButton('/Русский')]]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(menuLang, resize_keyboard=True, one_time_keyboard=True)
    msg = 'Խնդրում եմ ընտրել իմ լեզուն'
    dobby.send_message(chat_id=message.chat.id, text=msg, reply_markup=reply_kb_markup.to_json())
    
@dobby.message_handler(commands = ['English', 'Հայերեն', 'Русский'])
def setIdNameLang(message):
    lang = message.text[1:]

    queryGetLang = 'SELECT lang FROM subscribers WHERE chatID = %s'
    cursor.execute(queryGetLang, (message.chat.id, ))
    prev_lang = cursor.fetchone()
    
    if(prev_lang is None):
        querySetVals = 'INSERT INTO subscribers(chatID, fname, lang) VALUES (%s, %s, %s)'
        cursor.execute(querySetVals, (message.chat.id, message.chat.first_name, lang))
        outagesDB.commit()

        menuUtilities = utilitiesKboard[lang]
        reply_kb_markup = telegram.ReplyKeyboardMarkup(menuUtilities, resize_keyboard=True, one_time_keyboard=True)
        msg = startMessage[lang]
        dobby.send_message(chat_id=message.chat.id, text=msg, reply_markup=reply_kb_markup.to_json())
    else:
        queryChangeLang = 'UPDATE subscribers SET lang = %s WHERE chatID = %s'
        cursor.execute(queryChangeLang, (lang, message.chat.id))
        outagesDB.commit()

        # updating province with new lang
        queryGetProv = 'SELECT province FROM subscribers WHERE chatID = %s'
        cursor.execute(queryGetProv, (message.chat.id, ))
        prov = cursor.fetchone()[0]   #pay attention to this, can it be null?

        if prov is not None:
            for i in range(len(provinces[prev_lang[0]])):
                if provinces[prev_lang[0]][i] == prov:
                    prov = provinces[lang][i]
                    break

            queryChangeProv = 'UPDATE subscribers SET province = %s WHERE chatID = %s'
            cursor.execute(queryChangeProv, (prov, message.chat.id))
            outagesDB.commit()


        # updating utility with new lang
        queryGetUtil = 'SELECT utility FROM subscribers WHERE chatID = %s'
        cursor.execute(queryGetUtil, (message.chat.id, ))
        util = cursor.fetchone()[0]

        if util is not None:
            for i in range(len(utilities[prev_lang[0]])):
                if utilities[prev_lang[0]][i] == util:
                    util = utilities[lang][i]
                    break

            queryChangeUtil = 'UPDATE subscribers SET utility = %s WHERE chatID = %s'
            cursor.execute(queryChangeUtil, (util, message.chat.id))
            outagesDB.commit()

        msg = changedLangMessage[lang]
        dobby.send_message(chat_id=message.chat.id, text=msg)
        



@dobby.message_handler(commands = (utilities['English'] + utilities['Հայերեն'] + utilities['Русский']))
def setUtilities(message):
    querySetUtility = 'UPDATE subscribers SET utility = %s WHERE chatID = %s'
    util = message.text[1:]
    chat_id = message.chat.id
    cursor.execute(querySetUtility, (util, chat_id))
    outagesDB.commit()

    queryGetLang = 'SELECT lang FROM subscribers WHERE chatID = %s'
    cursor.execute(queryGetLang, (chat_id, ))
    lang = cursor.fetchall()[0][0]

    menuProvinces = provincesKboard[lang]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(menuProvinces, resize_keyboard=True, one_time_keyboard=True)
    msg = provMessage[lang]
    dobby.send_message(chat_id=message.chat.id, text=msg, reply_markup=reply_kb_markup.to_json())

@dobby.message_handler(commands = (provinces['English'] + provinces['Հայերեն'] + provinces['Русский']))
def setProvince(message):
    querySetProvince = 'UPDATE subscribers SET province = %s WHERE chatID = %s'
    prov = message.text[1:]
    chat_id = message.chat.id
    cursor.execute(querySetProvince, (prov, chat_id))
    outagesDB.commit()

    queryGetLang = 'SELECT lang FROM subscribers WHERE chatID = %s'
    cursor.execute(queryGetLang, (chat_id, ))
    lang = cursor.fetchall()[0][0]

    msg = greetMessage[lang]
    dobby.send_message(chat_id=message.chat.id, text=msg)


@dobby.message_handler(commands = ['help', 'օգնություն', 'помощь'])
def sendHelp(message):
    lang = getLang(helps, message.text[1:])
    msg = helpMessage[lang]
    dobby.send_message(chat_id=message.chat.id, text=msg)

@dobby.message_handler(commands = ['feedback', 'հետադարձ_կապ', 'обратная_связь'])
def sendFeedback(message):
    lang = getLang(feedbacks, message.text[1:])
    msg = feedbackMessage[lang]
    dobby.send_message(chat_id=message.chat.id, text=msg)

@dobby.message_handler(commands = ['unsubscribe', 'ապաբաժանորդագրվել', 'отписаться'])
def unsubscribe(message):
    queryDeleteData = 'DELETE FROM subscribers WHERE chatID = %s'
    cursor.execute(queryDeleteData, (message.chat.id, ))
    outagesDB.commit()

    lang = getLang(unsubscribes, message.text[1:])
    msg = ciaoMessage[lang]
    dobby.send_message(chat_id=message.chat.id, text=msg)

@dobby.message_handler(commands = ['see_my_data', 'տեսնել_իմ_տվյալները', 'посмотреть_мои_данные'])
def seeMyData(message):
    queryGetAllData = 'SELECT * FROM subscribers WHERE chatID = %s'
    cursor.execute(queryGetAllData, (message.chat.id, ))
    userData = cursor.fetchone()

    lang = getLang(seeMyDatas, message.text[1:])
    msg = f'{cols[lang][2]}: {userData[2]}, {cols[lang][3]}: {userData[3]}, {cols[lang][4]}: {userData[4]}, {cols[lang][5]}: {userData[5]}'
    dobby.send_message(chat_id=message.chat.id, text=msg)

outagesDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1029384756",
    database = "outagesDB"
)
cursor = outagesDB.cursor()

while True:
    try:
        dobby.polling()
    except Exception:
        time.sleep(15)





  




