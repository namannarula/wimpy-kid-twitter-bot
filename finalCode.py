from twython import Twython
from quotes import messages
import random
import time

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def final():
    message = random.choice(messages)
    twitter.update_status(status=message)
    print("Tweeted: {}".format(message))
    
while True:
    final()
    time.sleep(900)
