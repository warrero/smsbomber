import vk_api
import time

token = "Ваш токен"

vk = vk_api.VkApi(token=token)


vk._auth_token()

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет" or body.lower() == 'здарова':
            	vk.method("messages.send", {"peer_id": id, "message": "Привет!"})
	        elif body.lower() == 'пока':
	        	vk.method("messages.send", {"peer_id": id, "message": "Пока("})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "Не понял тебя! Напиши понятнее"})
    except Exception as E:
        time.sleep(1)
