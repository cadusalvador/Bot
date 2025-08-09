from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = os.getenv("SEATALK_WEBHOOK_URL")

@app.route("/", methods=["POST"])
def webhook():
    data = request.json

    print("Dados recebidos", data)

    if WEBHOOK_URL:
        payload = {"content": "Olá"}
        resp = requests.post(WEBHOOK_URL, json=payload)

        if resp.status_code == 200:
            print("Mensagme enviada com sucesso")
        else:
            print(f"Falha ao enviar: {resp.status_code} - {resp.text}")

    return jsonify({"status": "ok"}), 200

@app.route("/", methods=["GET"])
def home():
    return "Bot SeaTalk ativo!", 200 


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0.", port=port)
