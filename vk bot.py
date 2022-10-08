import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# Значит так, регаю группу в вк, беру оттуда ключ апи
token = "vk1.a.xI6OrHXJE2d-ctlqxZpsYYm5wDTvVlEi-zxHoGkAXD7_MPY04jZscnnaQDWZScyMJhWhMfNQwsxM6zSmRJLi1gimvq29h_GCSF_tThTly6uJFDKFUUBDV758C1WOEYZ3oRjU0YIwT-H_Tw2XodojBW-Qe58_tkWGU0DfCNbTPSty8pOu5C_Y-Sk-Z6m3tFy5"
id_group = '216356462'
# 3 строчки ниже это авторизация на сервере, пока сам не очень раздупляю, но рил всегда 100% нужно писать эти 3 строчки
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
LongPoll = VkLongPoll(vk_session, id_group)


# Функция для ведения диалога я не знаю зачем нужен random_id, но в гайдах написано, что так надо
def send_message(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


# Дальше, что у нас, цикл для того, что бы бот раздуплял сообщения
# Тут пока не работает(
while True:
    for event in LongPoll.listen():
        # формат реагирование на сообщение
        if event.type == VkEventType.MESSAGE_NEW:
            # Тут у нас реагирование сообщение от пользователей(что бы не было реакции на сообщения от самого себя)
            if event.to_me:
                # Переменная для распознования текста с маленькой буквы(Привет и привет для него будет одно и то же)
                message = event.text.lower()
                id = event.user_id
                # Наконец-то базар с ботом
                if message == "Привет":
                    # Это наша функция со словарем
                    send_message(id, 'Ты чо быдло?')
# И кста бот у меня не включился и я вообще не раздупляю, что делать, пока всё что я понял - это VkEventType, там разные приколы есть
# Можно реакцию на стикеры бахнуть или на видево
