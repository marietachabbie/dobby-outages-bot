import googlemaps
from datetime import datetime
import math

myApiKey = 'AIzaSyBAxkCS9lxQgZ5FOGZD598UZO9vYiPAx0Q'
gmaps = googlemaps.Client(key=myApiKey)
userLocation = gmaps.geocode('33 Aram Khachatrian Street, Yerevan, Armenia')

lat = userLocation[0]['geometry']['location']['lat']
lng = userLocation[0]['geometry']['location']['lng']
# userAddress = {'location': {'lat': lat, 'lng' : lng},
#                 'areaNear': {'north': {'lat': 456, 'lng': 789},
#                             'east': {'lat': 456, 'lng': 789},
#                             'west': {'lat': 456, 'lng': 789},
#                             'south': {'lat': 456, 'lng': 789}}
#                 }


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

