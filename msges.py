import telegram

startMessage = {'Հայերեն': '''Ողջույն, ես Դոբբին եմ` քո օգնական էլֆը: Ես օրվա ընթացքում մի քանի անգամ կստուգեմ կոմունալ ծառայությունների կայքերը եւ
քեզ տեղյակ կպահեմ քո հասցեում սպասվող անջատումների մասին: Որո՞նք են քեզ հետաքրքրում''',
                'English': '''Hi. I'm Dobby - your helper elf. I'll daily check the utility services' sites and inform you whenever I see
an announcement about coming outages in your address. What utility are you unterested in?''',
                'Русский': '''Привет. Я Добби - твой помощник-эльф. Я буду ежедневно проверять сайты коммунальных служб и сообщать тебе, когда увижу
объявление о предстоящих отключениях на твой адрес. Какая утилита тебя интересует?'''
            }

provMessage = {'Հայերեն': 'Ո՞ր մարզում',
            'English': 'In which province?',
            'Русский': 'В какой провинции?'
}

greetMessage = {'Հայերեն': 'Գրանցեցի: Կհանդիպենք, երբ մի բան գտնեմ 👌',
            'English': 'Registered. See you whenever I find anything. 👌',
            'Русский': 'Записал. Увидимся, когда я что-нибудь найду 👌'
}

helps = {'English': 'help', 'Հայերեն': 'օգնություն', 'Русский': 'помощь'}

helpMessage = {'Հայերեն': '''Ընտրիր` ինչ ես ուզում անել.
/փոխել_լեզուն
/փոխել_կոմունալը
/փոխել_քաղաքը
/փոխել_թաղամասը
/տեսնել_իմ_տվյալները
/հետադարձ_կապ
/ապաբաժանորդագրվել (🧦)''',
            'English': '''Tell me what do you want to do:
/change_language
/change_utility
/change_province
/change_district
/see_my_data
/feedback
/unsubcribe (🧦)''',
            'Русский': '''Выбирай что ты хочешь делать:
/изменить_язык
/изменить_утилиту
/изменить_провинцию
/изменить_район
/посмотреть_мои_данные
/обратная_связь
/отписаться (🧦)'''
} #user needs to copy paste the command in armenian and russian

feedbacks = {'English': 'feedback', 'Հայերեն': 'հետադարձ_կապ', 'Русский': 'обратная_связь'}

feedbackMessage = {'Հայերեն': 'Ցանկացած առաջարկ եւ/կամ բողոքի դեպքում կարող ես էլ. նամակ գրել dobbyarmbot@gmail.com հասցեին',
                'English': 'In case of any suggestion and/or complaint you could write an e-mail to dobbyarmbot@gmail.com address',
                'Русский': 'В случае каких-либо предложений и/или жалоб ты можешь написать по электронной почте dobbyarmbot@gmail.com'}

changedLangMessage = {'English': "From now on I'll talk to you in English 🙂",
            'Հայերեն': 'Այսուհետ ես քեզ հետ կխոսեմ հայերեն 🙂',
            'Русский': 'С этого момента я буду говорить с тобой по-русски 🙂'}

unsubscribes = {'English': 'unsubscribe', 'Հայերեն': 'ապաբաժանորդագրվել', 'Русский': 'отписаться'}

ciaoMessage = {'English': "I've deleted all you data. Hope to see you soon again 🤚",
            'Հայերեն': 'Ես ջնջել եմ քո բոլոր տվյալները: Հուսով եմ` շուտով նորից կհանդիպենք 🤚',
            'Русский': 'Я удалил все твои данные. Надеюсь скоро увидеть тебя снова 🤚'}

seeMyDatas = {'English': 'see_my_data', 'Հայերեն': 'տեսնել_իմ_տվյալները', 'Русский': 'посмотреть_мои_данные'}

cols = {'English': ['', '', 'name', 'language', 'utility', 'province', 'city', 'streets'],
        'Հայերեն': ['', '', 'անուն', 'լեզու', 'կոմունալ', 'մարզ', 'քաղաք', 'փողոցներ'],
        'Русский': ['', '', 'имя' , 'язык', 'утилита', 'провинция', 'город', 'улицы']}



utilities = {'Հայերեն': ['գազ', 'էլ. էներգիա', 'ջուր', 'բոլորը'],
            'English': ['gas', 'power', 'water', 'all'],
            'Русский': ['газ', 'электричество', 'вода', 'все']}

utilitiesKboard = {'Հայերեն': [[telegram.KeyboardButton('/էլ. էներգիա')], 
            [telegram.KeyboardButton('/ջուր')], [telegram.KeyboardButton('/բոլորը')]],
            'English': [[telegram.KeyboardButton('/power')],
            [telegram.KeyboardButton('/water')], [telegram.KeyboardButton('/all')]],
            'Русский': [[telegram.KeyboardButton('/электричество')],
            [telegram.KeyboardButton('/вода')], [telegram.KeyboardButton('/все')]]}

provinces = {'English': ['Yerevan', 'Aragatsotn', 'Ararat', 'Armavir',  'Gegharkunik', 'Kotayk', 'Lori',
            'Shirak', 'Syunik', 'Tavush', 'Vayots Dzor'],
            'Հայերեն': ['Երեւան', 'Արագածոտն', 'Արարատ', 'Արմավիր', 'Գեղարքունիք', 'Կոտայք', 'Լոռի', 
            'Շիրակ', 'Սյունիք', 'Տավուշ', 'Վայոց ձոր'],
            'Русский': ['Ереван', 'Арагацотн', 'Арарат', 'Армавир', 'Гегаркуник', 'Котайк', 'Лори', 
            'Ширак', 'Сюник', 'Тавуш', 'Вайоц-Дзор']
            }

provincesKboard = {'English':[[telegram.KeyboardButton('/Yerevan')], [telegram.KeyboardButton('/Aragatsotn')],
    [telegram.KeyboardButton('/Ararat')], [telegram.KeyboardButton('/Armavir')],
    [telegram.KeyboardButton('/Gegharkunik')], [telegram.KeyboardButton('/Kotayk')],
    [telegram.KeyboardButton('/Lori')], [telegram.KeyboardButton('/Shirak')],
    [telegram.KeyboardButton('/Syunik')], [telegram.KeyboardButton('/Tavush')],
    [telegram.KeyboardButton('/Vayots Dzor')]],

    'Հայերեն':[[telegram.KeyboardButton('/Երեւան')], [telegram.KeyboardButton('/Արագածոտն')],
    [telegram.KeyboardButton('/Արարատ')], [telegram.KeyboardButton('/Արմավիր')],
    [telegram.KeyboardButton('/Գեղարքունիք')], [telegram.KeyboardButton('/Լոռի')], 
    [telegram.KeyboardButton('/Կոտայք')], [telegram.KeyboardButton('/Շիրակ')],
    [telegram.KeyboardButton('/Սյունիք')], [telegram.KeyboardButton('/Վայոց ձոր')],
    [telegram.KeyboardButton('/Տավուշ')]],

    'Русский':[[telegram.KeyboardButton('/Ереван')], [telegram.KeyboardButton('/Арагацотн')],
    [telegram.KeyboardButton('/Арарат')], [telegram.KeyboardButton('/Армавир')],
    [telegram.KeyboardButton('/Вайоц-Дзор')], [telegram.KeyboardButton('/Гегаркуник')],
    [telegram.KeyboardButton('/Котайк')], [telegram.KeyboardButton('/Лори')],
    [telegram.KeyboardButton('/Сюник')], [telegram.KeyboardButton('/Тавуш')],
    [telegram.KeyboardButton('/Ширак')]]
}    



# {'English': '', 'Հայերեն': '', 'Русский': ''}

