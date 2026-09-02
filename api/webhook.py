import os
import fastapi
import requests_async

app = fastapi.FastAPI()
BOT_TOKEN = os.environ['BOT_TOKEN']

async def say(text, chat_id):
	await requests_async.post(
		f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage',
		json={
			'chat_id': chat_id,
			'text': f'{text}'
		}
	)

@app.post('/api/webhook')
async def webhook(request: fastapi.Request):
	json = await request.json()
	message = json.get('message')

	if not message:
		return 'OK'
	
	chat_id = message['chat']['id']
	text = message.get('text')

	say(text, chat_id)

	return 'OK'
