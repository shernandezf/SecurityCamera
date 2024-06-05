from twilio.rest import Client
import os
account_sid = os.getenv('account_sid_twilio')
auth_token = os.getenv('auth_token_twilio')
client = Client(account_sid, auth_token)
def sendSMS(mensaje):
    message = client.messages.create(
        from_='+12085511590',
        body=mensaje,
        to='+573208995663'
    )
    print(message.sid)

