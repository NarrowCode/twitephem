# Twitephem 
import twitter
import json
from _api import api_key, api_secret, acc_token, acc_secret

version = "1.0"
print("TWITEPHEM v%s" %  version)
print("Connecting to twitter API.")
api = twitter.Api(consumer_key=api_key,
                  consumer_secret=api_secret,
                  access_token_key=acc_token,
                  access_token_secret=acc_secret)


if api:
    print("Authentication successful.")
    print("Options: d     - Delete tweets")
    print("         dh    - Delete tweets & save history")
    sel = str(raw_input("Enter your selection and press enter: "))
    if(sel == "d" or sel == "dh"):
        statuses = api.GetUserTimeline(count=200)
        outf = open("history.txt","a")
        i = 1 
        for status in statuses:
            print(i, status.id, status.created_at_in_seconds)
            if (sel == "dh"):
                outf.write("{s_id};{s_t};{s_txt}\n".format(s_id = status.id,
                           s_t = status.created_at_in_seconds, 
                           s_txt = status.text.encode("utf-8")))
            i += 1
else:
    print("nay")
