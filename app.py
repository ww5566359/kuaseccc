from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('U2ft7oOQobM1CVXQL17cuoxb35w+XfAYJY89EP/TRUV89Y/GIXf0yJjlybUUJuJoBnyRji5HhpG2aDTQJQKZUZursXUca3KXjFV7ESoho+6WHv2dSQFdxyB/jpzaZkuF/8XVkUtS4Ha4ojG8tQ2hfQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('35b79be8e1a7e1c699feab3eabecbf05')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
