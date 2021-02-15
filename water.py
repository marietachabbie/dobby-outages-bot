import requests
from bs4 import BeautifulSoup
from datetime import date

def check_water():
    months = ['', 'հունվար', 'փետրվար', 'մարտ', 'ապրիլ', 'մայիս', 'հունիս',
    'հուլիս', 'օգոստոս', 'սեպտեմբեր', 'հոկտեմբեր', 'նոյեմբեր', 'դեկտեմբեր']

    source = requests.get('https://www.veolia.am/hy/consumers/jranjatowmner').text
    soup = BeautifulSoup(source, 'lxml')

    announcement = soup.find('div', class_='wysiwyg').text
    ann_list = announcement.split(' ')

    curr_mm = int(str(date.today())[5] + str(date.today())[6])
    curr_dd = int(str(date.today())[8] + str(date.today())[9])

    for i in range(len(ann_list)):
        if(len(ann_list[i]) > 0):
            word = ann_list[i].lower()
            if(word[-1] == 'ի'):
                word = word[:-1]

            if(word == months[curr_mm + 1]):
                return announcement
            elif(word == months[curr_mm]):
                ann_day = int(ann_list[i + 1][0] + ann_list[i + 1][1])
                if(curr_dd <= ann_day):
                    return announcement

