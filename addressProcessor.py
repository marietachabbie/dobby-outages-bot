import re
import string

def normalize(text):
    remove = string.punctuation.replace('/', '')
    pattern = r'[{}]'.format(remove)
    text = re.sub(pattern, "", text)
    return text

addresses = [
    {'province':'', 'district':'', 'street':'', 'buildings':[]}
]

announcement = open('announcement.txt', 'r')




