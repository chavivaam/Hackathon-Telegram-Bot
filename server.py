import requests
from flask import Flask, Response, request

from utils.config import BASE_TELEGRAM_URL
from controller.entities.bot import Bot
from controller.entities.message import Message


app = Flask(__name__, static_url_path='', static_folder='Downloads')


@app.route('/message', methods=["POST"])
def handle_message():
    req_as_json = request.get_json()
    msg = Message(req_as_json)
    ans = bot.handle_message(msg)
    res = requests.get("{}/sendMessage?chat_id={}&text={}"
                       .format(BASE_TELEGRAM_URL, msg.get_chat_id(), ans))
  
    return Response("success")


if __name__ == '__main__':
    bot = Bot()
    app.run(port=80)
