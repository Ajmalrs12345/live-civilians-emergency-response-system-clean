import time
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

def send_emergency_sms(account_sid, auth_token, from_number, to_number, message):
    """
    Send an emergency SMS using Twilio
    
    :param account_sid: Twilio Account SID
    :param auth_token: Twilio Auth Token
    :param from_number: Twilio phone number
    :param to_number: Recipient's phone number
    :param message: SMS message content
    :return: Boolean indicating success or failure
    """
    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)
        
        # Send message
        message = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        
        print(f"Emergency SMS sent successfully! SID: {message.sid}")
        return True
        
    except TwilioRestException as e:
        print(f"Error sending emergency SMS: {str(e)}")
        return False

# Optional countdown function if needed
def countdown(seconds):
    """
    Simple countdown function
    
    :param seconds: Number of seconds to countdown
    """
    while seconds > 0:
        print(f"Countdown: {seconds} seconds remaining")
        time.sleep(1)
        seconds -= 1