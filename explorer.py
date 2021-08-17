from twilio.rest import Client

# fill "" with numbers

client = Client("","")

# printing all of the messages

for msg in client.messages.list():
    print(msg.body)

# for deleting use msg.delete()
# creating a new message

message = client.messages.create(
    to="",
    from_="",
    body="This is a message sent"
)
print(f'Created a new message: {message.sid}')
