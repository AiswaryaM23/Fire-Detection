from twilio.rest import Client
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid ='AC4544a12103ec4839ab8d10b17fcd88c1'
auth_token ='9192ca5508269df7efc29b0b239ee288'
client = Client(account_sid, auth_token)
message = client.messages.create(
	body="FIRE ALERT!!",
    from_='+16067160811',
    to='+919074354819'
)
print(message.sid)