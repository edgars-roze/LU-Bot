import os
import fastapi
import telegram

api = fastapi.FastAPI()
BOT_TOKEN = os.environ['BOT_TOKEN']

bot = telegram.Bot(BOT_TOKEN)
app = telegram.Application.builder().token(BOT_TOKEN).build()

@api.post('/api/webhook')
async def webhook(request: fastapi.Request):
	json = await request.json()
	update = telegram.Update.de_json(json, bot)

	if update.message and update.message.text:
		await update.message.reply_text(update.message.text)

	return 'OK'
