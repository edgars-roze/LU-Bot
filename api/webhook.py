import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.environ["BOT_TOKEN"]


@app.post("/api/webhook")
def webhook():
    update = request.get_json()

    message = update.get("message")

    if not message:
        return "OK", 200

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": f"You said: {text}"
        }
    )

    return "OK", 200
