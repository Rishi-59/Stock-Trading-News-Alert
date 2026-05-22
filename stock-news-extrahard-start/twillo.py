# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
MY_NUMBER = os.getenv("MY_NUMBER")

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def send_sms(body):
    client = (TWILIO_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=body,
        from_="+14435656716",
        to=str(MY_NUMBER),
    )

    print(message.body)