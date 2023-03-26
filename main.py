## -*- coding: utf-8 -*-
import os

import openai
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

OPENAI_KEY = os.environ['OPENAI_KEY']
LINE_CHANNEL_SECRET = os.environ['LINE_CHANNEL_SECRET']
LINE_CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)
openai.api_key = OPENAI_KEY
conversation = []


def lambda_handler(event, _):

    signature = event["headers"]["x-line-signature"]
    body = event['body']

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        msg = "Invalid Signature"
        return {"statusCode": 400, "body": msg}

    return {"statusCode": 200, "body": "OK"}


def ask_chatgpt(q):

    question = {"role": "user", "content": q}
    conversation.append(question)

    completions = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=conversation
    )

    response = completions.choices[0].message.content
    answer = {"role": "assistant", "content": response}
    conversation.append(answer)

    return response


@handler.add(MessageEvent, message=(TextMessage))
def handling_message(event):
    replyToken = event.reply_token

    if isinstance(event.message, TextMessage):
        messages = event.message.text
        response = ask_chatgpt(messages)

        response_message = TextSendMessage(text=response)
        line_bot_api.reply_message(reply_token=replyToken, messages=response_message)
