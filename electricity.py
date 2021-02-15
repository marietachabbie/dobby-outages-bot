import requests
from bs4 import BeautifulSoup
from datetime import date

def getAnnouncement():
    source = requests.get('http://www.ena.am/Info.aspx?id=5&lang=1').text
    soup = BeautifulSoup(source, 'lxml')
    announcement = soup.find('span', id='ctl00_ContentPlaceHolder1_attenbody').text
    return announcement

def getUserAddress():
    add = input('please input your address: ')
    addList = add.split(' ')
    l = len(addList)
    userAdd = {'street': '', 'building': addList[l - 1]}
    for i in range(l - 1):
        userAdd['street'] += addList[i] + ' '
    userAdd['street'] = userAdd['strName'][:-1]
    
    return userAdd


def isFuture(ann):
    #an awkward way of doing this
    months = ['', 'հունվար', 'փետրվար', 'մարտ', 'ապրիլ', 'մայիս', 'հունիս',
    'հուլիս', 'օգոստոս', 'սեպտեմբեր', 'հոկտեմբեր', 'նոյեմբեր', 'դեկտեմբեր']
    curr_mm = int(str(date.today())[5] + str(date.today())[6])
    curr_dd = int(str(date.today())[8] + str(date.today())[9])
    # ann_list = announcement.split(' ')

    # for i in range(len(ann_list)):
    #     if(len(ann_list[i]) > 0):
    #         word = ann_list[i].lower()
    #         if(word[-1] == 'ի'):
    #             word = word[:-1]

    #         if(word == months[curr_mm + 1]):
    #             return announcement
    #         elif(word == months[curr_mm]):
    #             ann_day = int(ann_list[i + 1][0] + ann_list[i + 1][1])
    #             if(curr_dd <= ann_day):
    #                 return announcement
    pass

# azatamartikner 124
def findUserAddress(ann, address):
    street = address['street']
    building = address['building']

    announcement = ann.split(' ')
    for i in range(len(announcement)):
        if announcement[i] == street or announcement[i] == street + 'ի':
            for j in range(i + 1, 10):
                if (announcement[j] == 'փ' or announcement[j] == 'փ.' or announcement[j] == 'փող' or announcement[j] == 'փող.'
                    or announcement[j] == 'փողոց' or announcement[j] == 'պող.' or announcement[j] == 'պ.'
                    or announcement[j] == 'պողոտա'):
                    j += 1
                    

                if announcement[j][-1] == ',':
                    announcement[j] = announcement[j][:-1]
                    
                if announcement[j].isnumeric():
                    if announcement[j] == building or int(announcement[j]) == building:
                        return ann
                else:
                    if announcement[j] == building:
                        return ann
                    for k in range(len(announcement[j])):
                        if (announcement[j][k] == '-' or announcement[j][k] == ' - ' or announcement[j][k] == '- '
                            or announcement[j][k] == ' -'):
                            ran = announcement[j].split('-')
                            x = int(ran[0])
                            y = int(ran[1])
                            if building >= x and building <= y:
                                return ann
                            return 'not your building'
                    return ann
    return 'nothing in your address'


