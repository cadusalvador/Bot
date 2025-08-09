from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("SEATALK_BOT_TOKEN")

WEBHOOK_URL = os.getenv("SEATALK_WEBHOOK_URL")

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()

    print("Dados recebidos", data)

    if data.get("type") == "url_verification":
        return jsonify({"challenge": data["challenge"]})

    if data.get("type") == "message":
        text = data.get("text", "").strip()
        chat_id = data.get("chat_id")

        if text and chat_id:
            enviar_mensagem(chat_id, "Olá 👋")

    return jsonify({"status": "ok"})

def enviar_mensagem(chat_id, texto):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {BOT_TOKEN}" 
    }
    
    payload = {
        "chat_id": chat_id,
        "text": texto
    }

    requests.post(SEATALK_API_URL, headers=headers, json=payload)

@app.route("/", methods=["GET"])
def home():
    return "Bot SeaTalk ativo!", 200 


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0.", port=port)
