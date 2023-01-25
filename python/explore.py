from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Your Account SID"

# Your Auth Token from twilio.com/console
auth_token  = "Your Auth Token"

client = Client(account_sid, auth_token)


for msg in client.messages.list():
    print(msg)
