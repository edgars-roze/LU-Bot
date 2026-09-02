import os
import fastapi
import telegram

api = fastapi.FastAPI()
BOT_TOKEN = os.environ['BOT_TOKEN']

bot = telegram.Bot(BOT_TOKEN)
app = telegram.Application.builder().token(BOT_TOKEN).build()

async def help(update: telegram.Update, context):
	await update.message.reply_text(
		"No help"
	)

app.add_handler(telegram.CommandHandler('help', help))

@api.post('/api/webhook')
async def webhook(request: fastapi.Request):
	json = await request.json()
	await app.process_update(telegram.Update.de_json(json, bot))

	return 'OK'
