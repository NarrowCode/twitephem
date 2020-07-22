# Twitephem 
import twitter
from _api import api_key, api_secret, acc_token, acc_secret

api = twitter.Api(consumer_key=api_key,
                  consumer_secret=api_secret,
                  access_token_key=acc_token,
                  access_token_secret=acc_secret)


if api:
    statuses = api.GetUserTimeline()
    print([s.text for s in statuses])
else:
    print("nay")
