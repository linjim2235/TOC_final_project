from line_bot_api import *
from datetime import datetime
from linebot.models import MessageAction
from urllib.parse import parse_qsl

def service_category_event(event):
    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://example.com/image.jpg',
            title='Menu',
            text='Please select',
            actions=[
                PostbackAction(
                    label='postback',
                    display_text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageAction(
                    label='message',
                    text='message text'
                ),
                URIAction(
                    label='uri',
                    uri='http://example.com/'
                )
            ]
        )
    )

# def service_event(event):
#     data = dict(parse_qsl(event.postback.data))
#     bubbles = []
#     for service_id in services:
#         if services[service_id]['itemid'] == data['itemid']:
#             service = services[service_id]
#             bubble = {
#             }
#         bubbles.append(bubble)
#
#
#     flex_message = FlexSendMessage(
#         alt_text='hello',
#         contents={
#         "type": "carousel",
#         "contents": bubbles
#         }
#     )
#     line_bot_api.reply_message(
#         event.reply_token,
#         [flex_message]
#     )
#
def service_select_event(event):
    data = dict(parse_qsl(event.postback.data))
    quick_reply_buttons = []
    today = datetime.datetime.today().date()

    for x in range(1, 8):
        day = today + datetime.today(days=x)

        quick_reply_button = QuickReplyButton(
            action=PostbackAction(label=f'{day}',
                                  text=f'I would like to make an appointment for the day of {day}',
                                  data=f'action=select_time&service_id={data["service_id"]}&data={data}')
        )
        quick_reply_button.append(quick_reply_button)

    text_message = TextSendMessage(text='Hello, world',
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=MessageAction(label="label", text="text"))
                                   ]))
    line_bot_api.reply_message(
        event.reply_token,
        [text_message]
    )

# def service_select_time_event(event):
#     data = dict(parse_qsl(event.postback.data))
#     quick_reply_buttons = []
#     book_time = ['09:00', '11:00', '13:00', '15:00', '17:00']
#     for time in book_time:
#         quick_reply_button = QuickReplyButton(action=PostbackAction(label=time,
#                                                                     text=f'{time} this time',
#                                                                     data=f'action=confirm&service_id={data["service_id"]}&date={data["date"]}&time={time}'))
#         quick_reply_buttons.append(quick_reply_button)
#     text_message = TextSendMessage(text='Hello, world',
#                                    quick_reply=QuickReply(items=quick_reply_buttons))
#     line_bot_api.reply_message(
#         event.reply_token,
#         [text_message]
#     )
#
# def confirm_event(event):
#     data = dict(parse_qsl(event.postback.data))
#     booking_service = services[int(data['service_id'])]
#
#     confirm_template_message = TemplateSendMessage(
#         alt_text='Confirm template',
#         template=ConfirmTemplate(
#             text=f'Are you sure?\n\n{booking_service["title"]} {booking_service["duration"]}\ntime: {data["date"]} {data["time"]}\n\nOK or Not',
#             actions=[
#                 PostbackAction(
#                     label='OK',
#                     display_text='OK',
#                     data=f'action=confirmed&service_id={data["service_id"]}&date={data["date"]}&time={data["time"]}'
#                 ),
#                 MessageAction(
#                     label='NO',
#                     text='cancel'
#                 )
#             ]
#         )
#     )
#
#     line_bot_api.reply_message(
#         event.reply_token,
#         [confirm_template_message]
#     )