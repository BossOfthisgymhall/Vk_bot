import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = "vk1.a.xI6OrHXJE2d-ctlqxZpsYYm5wDTvVlEi-zxHoGkAXD7_MPY04jZscnnaQDWZScyMJhWhMfNQwsxM6zSmRJLi1gimvq29h_GCSF_tThTly6uJFDKFUUBDV758C1WOEYZ3oRjU0YIwT-H_Tw2XodojBW-Qe58_tkWGU0DfCNbTPSty8pOu5C_Y-Sk-Z6m3tFy5"
id_group = '216356462'
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkBotLongpoll(vk_session, id_group)

