from line_bot_api import *

def about_us_event(event):
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
            -@地址 會告訴您餐廳所在地-
            -@地址 會告訴您餐廳所在地""", emojis=emoji)
    sticker_message = StickerSendMessage(
        package_id='11538',
        sticker_id='51626494'
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message])
def location_event(event):
    location_message = LocationSendMessage(
        title="成大餐廳",
        address="701台南市東區大學路1號",
        latitude="22.9986085",
        longitude="120.2164195"
    )
    line_bot_api.reply_message(
        event.reply_token,
        location_message)