''' This module exports functions to generate tg-bot messages '''

# disable wrong-import-position warning
# pylint: disable = C0413

import os
import sys
from telebot import types

# set parent directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(f"{parent}/utils")

import constants

def generate_welcome_message(user_data):
    ''' generate welcome text and buttons for language choice '''
    lang = user_data.language_code
    user_name = user_data.first_name
    text = f"{constants.GREET[lang]}, {user_name}!\n{constants.ASK_LANG[lang]}"

    btnArmenian = types.InlineKeyboardButton(
        text= '🇦🇲 ' + constants.BTN_ARMENIAN,
        callback_data = 'lang' + '_' + constants.BTN_ARMENIAN)
    btnEnglish = types.InlineKeyboardButton(
        text = '🇬🇧 ' + constants.BTN_ENGLISH,
        callback_data = 'lang' + '_' + constants.BTN_ENGLISH)
    btnRussian = types.InlineKeyboardButton(
        text = '🇷🇺 ' + constants.BTN_RUSSIAN,
        callback_data = 'lang' + '_' + constants.BTN_RUSSIAN)

    markup = types.InlineKeyboardMarkup(
        ).add(btnEnglish, btnArmenian, btnRussian)

    return [text, markup]

def generate_share_location_message(lang):
    ''' generate message to ask to share location '''
    return constants.ASK_SHARE_LOCATION[lang]

def generate_ask_more_addresses(lang):
    ''' generate message to ask for more addresses or finish the setup '''
    text = constants.ASK_MORE_ADDRESSES[lang]

    btnMoreAdress = types.InlineKeyboardButton(
        text=constants.BTN_ANOTHER_ADDRESS[lang],
        callback_data = 'more')

    btnDone = types.InlineKeyboardButton(
        text=constants.BTN_DONE[lang],
        callback_data = 'done')

    markup = types.InlineKeyboardMarkup(
        ).add(btnMoreAdress, btnDone)

    return [text, markup]

def generate_finish_message(lang):
    ''' generate message to finish the setup '''
    return constants.FINISH[lang]
