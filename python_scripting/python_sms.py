from twilio.rest import Client

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.messages.create(
                                from="+19086766930",
                                body="This works!",
                                to="+18134389379"
                            )
print(message.sid)
