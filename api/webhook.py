import os
import requests
from fastapi import FastAPI, Request

app = FastAPI()

BOT_TOKEN = os.environ['BOT_TOKEN']

@app.post('/api/webhook')
async def webhook(request: Request):
	update = await request.get_json()
	message = update.get('message')

	if not message:
		return 'OK', 200

	chat_id = message['chat']['id']
	text = message.get('text', '')

	requests.post(
        f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage',
		json={
			'chat_id': chat_id,
			'text': f'{text}'
		}
	)

	return 'OK', 200
