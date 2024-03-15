''' This module exports telegram bot message handlers'''

# disable wrong-import-position warning
# pylint: disable = C0413

import os
import sys
from telebot import TeleBot

# set parent and other modules' directories
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(f'{parent}/utils')
sys.path.append(f'{parent}/temp_data_stocker')

import constants
import telegram_messages
from temp_data_storage import temp_data_stocker
import config

# initialize telegram bot
bot = TeleBot(config.BOT_TOKEN)

# initialize temporary data stocker
data_stocker = temp_data_stocker.TempDataStocker()

# global commands
@bot.message_handler(commands=[constants.HELP])
def send_help(message):
    ''' temp docstring '''
    bot.send_message(message.chat.id, '*** Here to help you! ***')

@bot.message_handler(commands=[constants.SETTINGS])
def send_settings(message):
    ''' temp docstring '''
    bot.send_message(message.chat.id, '*** Here comes your settings ***')

@bot.message_handler(commands=[constants.START])
def send_welcome(message):
    ''' greet user and ask for preferred language '''
    data_stocker.create_data_file(message)

    text, markup = telegram_messages.generate_welcome_message(message.from_user)
    bot.send_message(message.chat.id, text, reply_markup=markup)

def handle_callback_queries(callback_query):
    ''' handle callback queries from inline buttons '''
    data = callback_query.data.split('_')
    lang = data_stocker.read_language(callback_query.message)
    match data[0]:
        case 'lang':
            store_language_and_ask_address(data[1], callback_query.message)
        case 'address':
            ask_to_share_or_input_address(data[1], callback_query.message)
        case 'more':
            ask_for_address(lang, callback_query.message)
        case 'done':
            # TODO: store data from temp json to DB
            # TODO: rm temp json file
            finish_conversation(lang, callback_query.message)

@bot.callback_query_handler(handle_callback_queries)

@bot.message_handler(content_types=[constants.LOCATION])
def handle_location(message):
    ''' TODO: store user's location '''
    # message.location: {'longitude': 44.494431, 'latitude': 40.216256, ...}

    data_stocker.update_address(message)
    lang = data_stocker.read_language(message)
    ask_more_addresses_or_finish(message, lang)

@bot.message_handler(content_types=[constants.TEXT])
def handle_text_input(message):
    ''' temp docstring '''
    lang = data_stocker.read_language(message)
    if message.text.lower().startswith(constants.ADDRESS[lang]):
        # TODO: store user's location
        ask_more_addresses_or_finish(message, lang)
    else:
        handle_unknown_input(message, lang)

def ask_more_addresses_or_finish(message, lang):
    ''' ask if user wishes to add more addresses or not '''
    text, markup = telegram_messages.generate_ask_more_addresses(lang)
    bot.send_message(message.chat.id, text, reply_markup=markup)

def handle_unknown_input(message, lang):
    ''' handle all unknown inputs '''
    bot.send_message(message.chat.id, constants.UNKNOWN[lang])
    # TODO: send help

def store_language_and_ask_address(lang, message):
    ''' store user's preferred language in the chat's
    temporary json file and ask for address'''

    lang_code = constants.LANGUAGE_CODES[lang]
    data_stocker.update_language(message, lang_code)

    ask_for_address(lang_code, message)

def ask_for_address(lang, message):
    ''' aks if user wishes to share location or input manually '''
    text, markup = telegram_messages.generate_ask_address_message(lang)
    bot.edit_message_text(text, message.chat.id, message.id, reply_markup=markup)

def ask_to_share_or_input_address(btn_choice, message):
    ''' ask user to either share location or input address '''
    lang = data_stocker.read_language(message)
    if btn_choice == constants.BTN_LOCATION[lang]:
        bot.edit_message_text(
            telegram_messages.generate_share_location_message(lang),
            message.chat.id,
            message.id)
    elif btn_choice == constants.BTN_MANUAL[lang]:
        bot.edit_message_text(
            telegram_messages.generate_input_address_message(lang),
            message.chat.id,
            message.id)

def finish_conversation(lang, message):
    ''' finish the conversation '''
    text = telegram_messages.generate_finish_message(lang)
    bot.send_message(message.chat.id, text)
