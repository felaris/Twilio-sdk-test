from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2a7c23dc33b299ebd312a453c9adb7b8"

# Your Auth Token from twilio.com/console
auth_token  = "bc4ff5f356d4a11a1f18c88d0801b78d"

client = Client(account_sid, auth_token)


for msg in client.messages.list():
    print(msg)
