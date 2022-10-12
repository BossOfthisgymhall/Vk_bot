import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
TOKEN = "vk1.a.xI6OrHXJE2d-ctlqxZpsYYm5wDTvVlEi-zxHoGkAXD7_MPY04jZscnnaQDWZScyMJhWhMfNQwsxM6zSmRJLi1gimvq29h_GCSF_tThTly6uJFDKFUUBDV758C1WOEYZ3oRjU0YIwT-H_Tw2XodojBW-Qe58_tkWGU0DfCNbTPSty8pOu5C_Y-Sk-Z6m3tFy5"

session = vk_api.VkApi(token=TOKEN)


def send_message(user_id, message, keyboard=None):
	post = {
			"user_id": user_id,
			"message": message,
			"random_id": 0
			}
	if keyboard != None:
		post["keyboard"] = keyboard.get_keyboard()
	else:
		post = post
	session.method("messages.send", post)


for event in VkLongPoll(session).listen():
	if event.type == VkEventType.MESSAGE_NEW and event.to_me:
		text = event.text.lower()
		user_id = event.user_id

		if text == 'start':
			keyboard = VkKeyboard()
			keyboard.add_button("button", VkKeyboardColor.SECONDARY)
			keyboard.add_button("button", VkKeyboardColor.PRIMARY)
			keyboard.add_button("button", VkKeyboardColor.NEGATIVE)

			send_message(user_id, "РА СЕ Я", keyboard)