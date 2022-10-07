import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
#Значит так, регаю группу в вк, беру оттуда ключ апи
token = "vk1.a.xI6OrHXJE2d-ctlqxZpsYYm5wDTvVlEi-zxHoGkAXD7_MPY04jZscnnaQDWZScyMJhWhMfNQwsxM6zSmRJLi1gimvq29h_GCSF_tThTly6uJFDKFUUBDV758C1WOEYZ3oRjU0YIwT-H_Tw2XodojBW-Qe58_tkWGU0DfCNbTPSty8pOu5C_Y-Sk-Z6m3tFy5"
id_group = '216356462'
# 3 строчки ниже это авторизация на сервере, пока сам не очень раздупляю, но рил всегда 100% нужно писать эти 3 строчки
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkBotLongpoll(vk_session, id_group)

# Дальше, что у нас, цикл для того, что бы бот раздуплял сообщения
for event in longpoll.listen():
    # Тут у нас реагирование на сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        #Тут у нас реагирование сообщение от пользователей(что бы не было реакции на сообщения от самого себя)
        if event.to_me:
            #Переменная для распознования текста с маленькой буквы(Привет и привет для него будет одно и то же)
            message = event.text.lower()
            id.event

