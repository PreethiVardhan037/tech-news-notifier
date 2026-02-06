from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, WHATSAPP_CONTENT_SID
client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)

def send_news_as_whatsapp_message(to,msg):
    try:
        message = client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            to=to,
            body=msg
        )
        print(message.status,message.sid)
    except TwilioRestException as e:
        print(f"Error code: {e.code}\nError msg:{e.msg}")

