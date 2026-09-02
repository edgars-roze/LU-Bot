import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]


def handler(request):
    update = request.get_json()

    message = update.get("message")

    if not message:
        return {
            "statusCode": 200,
            "body": "OK"
        }

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": f"You said: {text}"
        }
    )

    return {
        "statusCode": 200,
        "body": "OK"
    }
