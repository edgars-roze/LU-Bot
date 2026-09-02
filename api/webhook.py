import os
import fastapi
import requests_async

app = fastapi.FastAPI()
BOT_TOKEN = os.environ['BOT_TOKEN']

async def say(chat_id, text):
	await requests_async.post(
		f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage',
		json={
			'chat_id': chat_id,
			'text': text
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

	await say(chat_id, 
		'''
		text
		text
		text
		'''
	)

	return 'OK'
