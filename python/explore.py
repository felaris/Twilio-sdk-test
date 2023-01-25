from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Your Account SID"

# Your Auth Token from twilio.com/console
auth_token  = "Your Auth Token"

client = Client(account_sid, auth_token)

# Check messages sent
''' for msg in client.messages.list():
    print(msg.body) '''


# Create and send message
#msg = client.messages.create(to="number", from_="number",body="The message you want to send",)

# To deleted your messages 
''' for msg in client.messages.list():
    print(f"Deleting {msg.body}")
    msg.delete()   '''