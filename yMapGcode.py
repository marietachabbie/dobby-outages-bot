import requests
from bs4 import BeautifulSoup
import json

def levDist(str1, str2):
    h = len(str1) + 1
    w = len(str2) + 1

    if h < w:
        for i in range((w -h)):
            str1 += ' '
    elif w < h:
        for i in range((h - w)):
            str2 += ' '

    edits = [[x for x in range(w)] for y in range(h)]
    for i in range(1, h):
        edits[i][0] = edits[i - 1][0] + 1
    for i in range(1, h):
        for j in range(1, w):
            if str2[i - 1] == str1[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = 1 + min(edits[i - 1][j - 1], edits[i][j - 1], edits[i - 1][j])
    return edits[-1][-1]

def getMostSimilar(string, listOfStrings):
    minDist = 0
    index = '-'

    for i in range(len(listOfStrings)):
            currDist = levDist(string, listOfStrings[i])
            if currDist < minDist or minDist == 0:
                index = i
                minDist = currDist
    return index

def getPossibleAddresses(reqAdd, myApiKey = '4a1bbdeb-237e-4601-a981-4b847eceeb64'):
    source = requests.get(f'https://geocode-maps.yandex.ru/1.x/?format=json&apikey={myApiKey}&geocode={reqAdd}&lang=en_US').json()

    # print(source)
    res = []
    found = len(source['response']['GeoObjectCollection']['featureMember'])
    for i in range(found):
        add = source['response']['GeoObjectCollection']['featureMember'][i]['GeoObject']
        if add['metaDataProperty']['GeocoderMetaData']["Address"]["country_code"] == "AM":
            res.append({'address': add['name'] + ', ' + add['description'], 'lat':add['Point']['pos'].split(' ')[1], 'lng':add['Point']['pos'].split(' ')[0]})
    return res

def getExactAddress(reqAdd):
    possibles = getPossibleAddresses(reqAdd)
    res = []
    for details in possibles:
        res.append(details['address'])
    
    index = getMostSimilar(reqAdd, res)
    if index != '-':
        return possibles[index]
    else:
        return "Couldn't find your address"

# change postal code to this -> 'AddressDetails': {'Country': {'AddressLine': 'Guadeloupe, Pointe-à-Pitre', 'CountryNameCode': 'GP', 'CountryName': 'Guadeloupe',
print(getExactAddress('Keru+Street'))

# # this takes too long to calculate
# radius = 100.0
# N = 10
# circlePoints = []
# for k in range(N):
#     angle = math.pi*2*k/N
#     dx = radius*math.cos(angle)
#     dy = radius*math.sin(angle)
#     point = {}
#     point['lat']= lat + (180/math.pi)*(dy/6378137)
#     point['lon']= lng + (180/math.pi)*(dx/6378137)/math.cos(lat*math.pi/180)
#     circlePoints.append(point)

# for p in circlePoints:
#     print(p['lat'], end=', ')
#     print(p['lon'])

