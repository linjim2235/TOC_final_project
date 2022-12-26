from flask import Flask, request, abort
from extensions import db, migrate
from models.user import User
from line_bot_api import *
from events.basic import about_us_event, location_event

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:123123000@localhost:5432/LineBot"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate.init_app(app, db)

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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = str(event.message.text).lower()
    user = User.query.filter(User.line_id == event.source.user_id).first()
    if not user:
        profile = line_bot_api.get_profile(event.source.user_id)

        user = User(line_id=profile.user_id, display_name=profile.display_name, picture_url=profile.picture_url)
        db.session.add(user)
        db.session.commit()
    if message_text == "@關於":
        about_us_event(event)
    elif message_text == "@地址":
        location_event(event)
    # elif message_text == "@預約":
    #     text_message = TextSendMessage(text="請輸入您要的時間、日期")
    else:
        emoji = [
            {
                "index": 0,
                "productId": "5ac1bfd5040ab15980c9b435",
                "emojiId": "024"
            },
            {
                "index": 12,
                "productId": "5ac1bfd5040ab15980c9b435",
                "emojiId": "034"
            }
        ]
        text_message = TextSendMessage(text="$ 不好意思，我不清楚 $", emojis=emoji)
        sticker_message = StickerSendMessage(
            package_id='6632',
            sticker_id='11825375'
        )
        line_bot_api.reply_message(
            event.reply_token,
            [text_message, sticker_message])

@handler.add(FollowEvent)
def handle_follow(event):
    emoji = [
        {
            "index": 0,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "001"
        },
        {
            "index": 18,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "056"
        }
    ]
    text_message = TextSendMessage(text="""$ 歡迎加入【成大餐廳】的官方帳號 $
    -您有以下功能可以使用-
    -@關於 會告訴您有哪些功能可以使用-
    -@地址 會告訴您餐廳所在地-""", emojis=emoji)
    sticker_message = StickerSendMessage(
        package_id='11538',
        sticker_id='51626494'
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message])

@handler.add(UnfollowEvent)
def handle_follow(event):
    print(event)
if __name__ == "__main__":
    app.run()