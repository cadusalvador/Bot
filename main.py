import hashlib
import json
from typing import    Dict, Any
from flask import Flask, request,jsonify
import requests
import os

WEBHOOK_URL = os.getenv("SEATALK_WEBHOOK_URL")
SIGNING_SECRET = os.getenv("SEATALK_SIGN_SECRET")
EVENT_VERIFICATION = os.getenv("SEATALK_EVENT_VERIFICATION")

app = Flask(__name__)


def is_valid_signature(signing_secret: bytes, body: bytes, signature: str) -> bool:
    # ref: https://open.seatalk.io/docs/server-apis-event-callback
    return hashlib.sha256(body + signing_secret).hexdigest() == signature


@app.route("/bot-callback", methods=["POST"])
def bot_callback_handler():
    body: bytes = request.get_data()
    signature: str = request.headers.get("signature")
    # 1. validate the signature
    if not is_valid_signature(SIGNING_SECRET, body, signature):
        return ""
    # 2. handle events
    data: Dict[str, Any] = json.loads(body)
    event_type: str = data.get("event_type", "")
    if event_type == EVENT_VERIFICATION:
        return data.get("event")

@app.route("/", methods=["POST"])
def webhook():
    data = request.json

    print("Dados recebidos:", data)

    if WEBHOOK_URL:
        payload = {"content": "WAAAALLL-E"}
        resp = requests.post(WEBHOOK_URL, json=payload)

        if resp.status_code == 200:
            print("Mensagem enviada com sucesso!")
        else:
            print(f"Falha ao enviar: {resp.status_code} - {resp.text}")

    return jsonify({"status": "OK"}), 200

@app.route("/", methods=["GET"])
def home():
    return "Bot Seatalk ativo!", 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
