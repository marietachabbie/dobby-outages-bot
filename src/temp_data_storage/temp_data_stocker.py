''' this module exports TempDataStocker that is supposed to store
temporary data of user for the session. JSON files should be
deleted once stored in database '''

import os
import json

class TempDataStocker:
    ''' stores temporary data '''

    def generate_data_filename(self, user_id):
        ''' generates temp json filename for a user '''
        current_dir = os.path.dirname(os.path.realpath(__file__))
        return f'{current_dir}/data/{user_id}_data.json'

    def generate_chat_data(self, message):
        ''' generates chat/user data '''
        return {
            'tg_user_id': message.from_user.id,
            'lang_code': message.from_user.language_code,
        }

    def create_data_file(self, message):
        ''' creates temporary json file '''
        file_path = self.generate_data_filename(message.from_user.id)
        data = self.generate_chat_data(message)
        with open(file_path, 'w+', encoding='utf-8') as file:
            json.dump(data, file)
        file.close()

    def update_language(self, message, lang):
        ''' updates language user has chosen '''
        file_path = self.generate_data_filename(message.from_user.id)
        data = json.load(open(file_path, 'r', encoding='utf-8'))
        data['lang_code'] = lang

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)
            file.close()


    def read_language(self, message):
        ''' reads user's chosen language from json file '''
        file_path = self.generate_data_filename(message.from_user.id)
        data = json.load(open(file_path, 'r', encoding='utf-8'))
        return data['lang_code'] if 'lang_code' in data else '' # maybe default language?

    def update_address(self, message):
        ''' updates user's address in temp json file '''
        file_path = self.generate_data_filename(message.from_user.id)
        data = json.load(open(file_path, 'r', encoding='utf-8'))

        location = {
            "longitude": message.location.longitude,
            "latitude": message.location.latitude,
        }

        if not 'address' in data:
            data['address'] = []

        data['address'].append(location)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)
            file.close()

    def delete_data_file(self, message):
        ''' deletes temporary json file '''
        # TODO: implement
