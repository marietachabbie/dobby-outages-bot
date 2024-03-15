''' This module exports constant values '''

# telegram commands
START = 'start'
HELP = 'help'
SETTINGS = 'settings'
TEXT = 'text'
LOCATION = 'location'

# language codes
LANGUAGE_CODES = {
    'Հայերեն': 'hy',
    'English': 'en',
    'Русский': 'ru',
}

# telegram buttons
BTN_ARMENIAN = 'Հայերեն'
BTN_ENGLISH = 'English'
BTN_RUSSIAN = 'Русский'

BTN_LOCATION = {
    'hy': 'կիսվել գտնվելու վայրով',
    'en': 'share location',
    'ru': 'поделиться местоположением',
}

BTN_MANUAL = {
    'hy': 'մուտքագրել',
    'en': 'input',
    'ru': 'вводить',
}

BTN_ANOTHER_ADDRESS = {
    'hy': 'եւս մեկ հասցե',
    'en': 'another address',
    'ru': 'другой адрес',
}

BTN_DONE = {
    'hy': '✅ ավարտել',
    'en': '✅ done',
    'ru': '✅ готово',
}

# telegram messaages
GREET = {
    'en': 'Hello',
    'ru': 'Здравствуйте',
}

ASK_LANG = {
    'en': 'What language do you wish to receive your notifications in?',
    'ru': 'На каком языке Вы хотите получать уведомления?',
}

ASK_ADDRESS = {
    'hy': 'Նախընտրում եք կիսվե՞լ Ձեր գտնվելու վայրով, թե՞ մուտքագրել այն ձեռքով',
    'en': 'Prefer to share your location or input it manually?',
    'ru': 'Предпочитаете поделиться своим местоположением или ввести его вручную?',
}

ASK_SHARE_LOCATION = {
    'hy': 'Կիսեք Ձեր գտնվելու վայրը Telegram-ի գործիքի միջոցով',
    'en': 'Share your location using the Telegram tool',
    'ru': 'Поделитесь своим местоположением с помощью инструмента Telegram',
}

ASK_INPUT_ADDRESS = {
    'hy': 'Մուտքագրեք Ձեր հասցեն այստեղ և սկսեք «Հասցե» բառով: \
    Օրինակ`\nՀասցե՝ Երևան, Արամի փողոց 1',
    'en': 'Input your address here and please start with the word "Adress". \
    Example:\nAddress: Yerevan, Aram Street 1',
    'ru': 'Введите здесь свой адрес и начните со слова «Адрес». \
    Пример:\nАдрес: Ереван, улица Арама 1',
}

ASK_MORE_ADDRESSES = {
    'hy': 'Ցանկանու՞մ եք ավելացնել նոր հասցե, թե՞ այսքանը բավական է',
    'en': 'Wish to add a new address or that\'s enough?',
    'ru': 'Хотите добавить новый адрес или этого достаточно?',
}

ADDRESS = {
    'hy': 'հասցե',
    'en': 'address',
    'ru': 'адрес',
}

UNKNOWN = {
    'hy': 'Ներողություն, ես Ձեզ չեմ հասկանում',
    'en': 'I am sorry, I don\'t understand you',
    'ru': 'Извините, я Вас не понимаю',
}

FINISH = {
    'hy': 'Այստեղից ես կշարունակեմ: \
Այժմ հետ նստեք և վստահ եղեք, որ ես կծանուցեմ, երբ մոտակայքում անջատում լինի:',
    'en': 'I\'ll take it from here. \
Now sit tight and rest assured you will be notified when there is an outage near you!',
    'ru': 'Дальше уже на меня. \
А теперь расслабьтесь и будьте уверены, что будете уведомлены, когда рядом будет \
отключение!',
}