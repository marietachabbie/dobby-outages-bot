''' this module interacts with database
to register and update user data '''

# disable wrong-import-position warning
# pylint: disable = C0413, C0411

import os
import sys
import json
import psycopg2

# set parent and other modules' directories
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import config

class DatabaseManager:
    ''' manages database interactions '''
    def __init__(self):
        try:
            self.connection = psycopg2.connect(database = config.DATABASE,
                            host = config.DB_HOST,
                            user = config.DB_USER,
                            password = config.DB_PASSWORD,
                            port = config.DB_PORT)
            self.cursor = self.connection.cursor()
        except psycopg2.OperationalError as e:
            print("Failed to connect to database:")
            print(e)

    def disconnect(self):
        ''' disconnects from database '''
        if self.connection:
            self.connection.close()
            print("Disconnected from database.")

    def get_one(self, tg_user_id):
        ''' gets single raw by tg_user_id '''
        query = "SELECT * FROM users where tg_user_id = %s"
        self.cursor.execute(query, (tg_user_id,))
        return self.cursor.fetchone()

    def insert_one(self, user_data):
        ''' inserts single raw into 'users' table '''
        tg_user_id, username, lang_code, addresses = user_data.values()
        query = "INSERT INTO users (tg_user_id, username, lang_code, addresses)\
                VALUES(%s, %s, %s, %s) RETURNING id"
        self.cursor.execute(query, (tg_user_id, username, lang_code, json.dumps(addresses)))
        raws = self.cursor.fetchone()
        self.connection.commit()
        print("Inserted into database", raws[0])
        return raws[0]
