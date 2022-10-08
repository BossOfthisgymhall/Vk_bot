#import vk_api
#from vk_api.longpoll import VkLongPoll, VkEventType

# Значит так, регаю группу в вк, беру оттуда ключ апи
#token = "vk1.a.xI6OrHXJE2d-ctlqxZpsYYm5wDTvVlEi-zxHoGkAXD7_MPY04jZscnnaQDWZScyMJhWhMfNQwsxM6zSmRJLi1gimvq29h_GCSF_tThTly6uJFDKFUUBDV758C1WOEYZ3oRjU0YIwT-H_Tw2XodojBW-Qe58_tkWGU0DfCNbTPSty8pOu5C_Y-Sk-Z6m3tFy5"
#id_group = '216356462'
# 3 строчки ниже это авторизация на сервере, пока сам не очень раздупляю, но рил всегда 100% нужно писать эти 3 строчки
#vk_session = vk_api.VkApi(token=token)
#session_api = vk_session.get_api()
#LongPoll = VkLongPoll(vk_session, id_group)


# Функция для ведения диалога я не знаю зачем нужен random_id, но в гайдах написано, что так надо
#def send_message(id, text):
 #   vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


# Дальше, что у нас, цикл для того, что бы бот раздуплял сообщения
# Тут пока не работает(

 #   for event in LongPoll.listen():
        # формат реагирование на сообщение
 #       if event.type == VkEventType.MESSAGE_NEW:
            # Тут у нас реагирование сообщение от пользователей(что бы не было реакции на сообщения от самого себя)
 #           if event.to_me:
                # Переменная для распознования текста с маленькой буквы(Привет и привет для него будет одно и то же)
 #               message = event.text.lower()
#                id = event.user_id
                # Наконец-то базар с ботом
 #               if message == "Привет":
                    # Это наша функция со словарем
#                    send_message(id, 'Ты чо быдло?')
# И кста бот у меня не включился и я вообще не раздупляю, что делать, пока всё что я понял - это VkEventType, там разные приколы есть
# Можно реакцию на стикеры бахнуть или на видево
#нашёл в интернетах этот пример, он работает, почему? я не знаю
import random
import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from bs4 import BeautifulSoup

api_key ="vk1.a.xI6OrHXJE2d-ctlqxZpsYYm5wDTvVlEi-zxHoGkAXD7_MPY04jZscnnaQDWZScyMJhWhMfNQwsxM6zSmRJLi1gimvq29h_GCSF_tThTly6uJFDKFUUBDV758C1WOEYZ3oRjU0YIwT-H_Tw2XodojBW-Qe58_tkWGU0DfCNbTPSty8pOu5C_Y-Sk-Z6m3tFy5"


session = requests.Session()
vk_session = vk_api.VkApi(token=api_key)
try:
    vk_session._auth_token()
except vk_api.AuthError as error_msg:
    print(error_msg)
    exit(0)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.from_user:  # Если написали в ЛС
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    message='Ваш текст', random_id=random.randint(1, 10000))
            if event.from_chat:  # Если написали в Беседе
                vk.messages.send(  # Отправляем собщение
                    chat_id=event.chat_id,
                    message='Ваш текст', random_id=random.randint(1, 10000))
                print("asdasdasdasdasdasdasdasdasdsa")