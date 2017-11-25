#Using Python 2.7 Not 3
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC31773b8d49a9f2fa717633754d5f4eeb"

# Your Auth Token from twilio.com/console
auth_token  = "55b10014f39a5fba8cddbf48ac99bebb"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+0201114767290",
    from_="+1 917-708-8308",
    body="Kareem, have no balance right now.")

print message.sid
