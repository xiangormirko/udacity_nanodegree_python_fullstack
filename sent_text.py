from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account

account_sid = "AC79210f42346cd4a0432a524e8c474752"
auth_token  = "e336e03ab08535d4068430233fbc4730"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi Stenko, I sent this text with some code that I wrote, good morning!",
    to="+16178181193",    # Replace with your phone number
    from_="+16178986322") # Replace with your Twilio number
print (message.sid)
