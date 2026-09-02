import os
import requests

BOT_TOKEN = os.environ['BOT_TOKEN']

def handler(request):
	message = request.get_json().get('message')
	chat_id = message['chat']['id']
	text = message['text']

	requests.post(
		f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
		json={
			"chat_id": chat_id,
			"text": f"You said: {text}"
		}
	)
