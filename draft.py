import re
import string

def normalize(text):
    remove = string.punctuation.replace('/', '')
    pattern = r'[{}]'.format(remove)
    re.sub(pattern, "", text)

    return text


 

def charArmToEng(word):
    charDict = {
        'ա':'a', 'բ':'b', 'գ':'g', 'դ':'d', 'ե':'e', 'զ':'z',
        'է':'e', 'ը':'e', 'թ':'t', 'ժ':'j', 'ի':'i', 'լ':'l',
        'խ':'kh', 'ծ':'ts', 'կ':'k', 'հ':'h', 'ձ':'dz', 'ղ':'gh',
        'ճ':'ch', 'մ':'m', 'յ':'y', 'ն':'n', 'շ':'sh', 'ո':'o',
        'չ':'ch', 'պ':'p', 'ջ':'j', 'ռ':'r', 'ս':'s', 'վ':'v',
        'տ':'t', 'ր':'r', 'ց':'ts', 'ու':'u', 'փ':'p', 'ք':'k',
        'և':'ev', 'օ':'o', 'ֆ':'f', '/':'/',
    }

    translit = ''
    for i in range(len(word)):
        if i == 0 and word[i] == 'ե':
            translit += 'ye'
        elif word[i] == 'ո' and word[i + 1] == 'ւ':
            translit += charDict['ու']
        elif word[i] == 'ւ':
            continue
        elif word[i].isnumeric():
            translit += word[i]
        elif word[i] in charDict:
            translit += charDict[word[i]]

    return translit

def translateArmToEng(completeAddressArm):
    # the fuck is տնատիրությունների?
    wordDict = {
        'քանաքեռ':'qanaqer',
        'փողոց':'street',
        'պողոտա':'avenue',
        'թաղամաս':'district',
        'շրջան':'district',
        'վարչական':'the+administrative+of', # of is in a wrong place 
        'գյուղ':'village',
        'մարզ':'region',
        'միկրոշրջան':'microdistrict',
        'սեփական':'private',
        'տուն':'house',
        'շենք':'building',
        'նրբանցք':'street lane',
        'խճուղի':'highway',
        'զանգված':'residential area', #nor nork's zangvacs
        'համայնք':'', #yeghvard hamaynq ?
        'քաղաք':'city',
        'և':'and',
        'հէկ':'',
        'սպը':'',
        'ընկերություն':'',
        'բժշկական':'',
        'կենտրոն':'',
        'անցուղու':'',
        'հարակից':'',
        'ոչ':'',
        'բնակիչ':'',
        'բաժանորդները':'',
        'դպրոցի':'',
        'մանկապարտեզ':'',
        'ձյունաշող':'dzunashogh',
        'բեխ':'bex',
        'մասնակի':'',
        'աձ':'', #ԱՁՆ-երը
        'հեռուստակենտրոն':'',
        'անվան':'',
        'պետական':'',
        'թատրոնի':'',
        'օպերայի':'',
        'բալետի':'',
        'համալսարանի':'',
        'թիվ':'',
        'հիվանդանոց':'',
        'վերականգնողական':''
    }

    completeAddressEng = ''
    word = ''
    for i in range(len(completeAddressArm)):
        if completeAddressArm[i] == ' ':
            if word in wordDict:
                completeAddressEng += wordDict[word].title()
            else:
                completeAddressEng += charArmToEng(word).title()
            completeAddressEng += '+'
            word = ''
        else:
            word += completeAddressArm[i]

    return completeAddressEng


####### spell checker with Norvig ###############

def edits1(word):
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    possibles = set(deletes + transposes + replaces + inserts)
    return possibles

def edits2(word): return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def known(words): return set(w for w in words if w in WORDS)

def correction(word): return max(candidates(word), key=P)

def candidates(word): 
    return known([word]) or known(edits1(word)) or known(edits2(word)) or [word]

# myFile = open('villagesAragatsotn.txt', 'r')
# data = set(myFile.read().split('\n'))
# print('Աշնակ' in data)
