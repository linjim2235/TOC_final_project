from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, LocationSendMessage, FollowEvent, UnfollowEvent,
TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn, PostbackAction, PostbackEvent, FlexSendMessage,
QuickReply, QuickReplyButton, ConfirmTemplate, ButtonsTemplate, URIAction
)

line_bot_api = LineBotApi('eSVk/98ZjxvW5BCadHNdyNw/6c6oPWjSGSxYaaQJDMuY0/Isu3khwnfaNa+XeEquayAxsmAnK2rdOPtNxrF1ARgcaSXzuQ5ire4uxiustRuVN16XHGblwLMMiGtOeFW76Du4xdLEJQ/MuDqi7kYf7QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('12cc7e59f5a0445db01500806d70abe1')