# подключение библеотек
import vk_api 
import time

token = "Ваш токен" # Токен можно достать в своей группе

vk = vk_api.VkApi(token=token) # тут наверное всем ясно


vk._auth_token() # авторизация

while True: 
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1: # если сообщений больше или равно 1, то выполняется условие
		id = messages["items"][0]["last_message"]["from_id"]
		body = messages["items"][0]["last_message"]["text"]
		#принимает на нижнем регистре
		if body.lower() == "привет" or body.lower() == 'здарова':
		   vk.method("messages.send", {"peer_id": id, "message": "Привет!"})
		elif body.lower() == 'пока':
		   vk.method("messages.send", {"peer_id": id, "message": "Пока("})
		# если придет непонятное сообщение боту, то выполнится else
		else:
		   vk.method("messages.send", {"peer_id": id, "message": "Не понял тебя! Напиши понятнее"})
    except Exception as E:
        time.sleep(1)
