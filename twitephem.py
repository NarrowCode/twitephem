# Twitephem 
import twitter
import json
import time
from datetime import datetime
from _api import api_key, api_secret, acc_token, acc_secret

VERSION = "1.0"
DATE_FORMAT = '%d-%m-%Y'

print("TWITEPHEM v%s" % VERSION)
print("Connecting to twitter API.")
api = twitter.Api(consumer_key=api_key,
                  consumer_secret=api_secret,
                  access_token_key=acc_token,
                  access_token_secret=acc_secret)


if api:
    print("Authentication successful.")
    print("Options: d       - Delete tweets")
    print("         dh      - Delete tweets & save history")
    print("         v       - View tweets")
    sel = str(raw_input("Enter your selection and press enter: "))
    if(sel == "d" or sel == "dh" or sel == "v"):
        start_date = str(raw_input("Please specify a start date in the form [DD-MM-YYYY]. " \
                                   "Tweets after this date will be queried: "))
        start_date_obj = datetime.strptime(start_date, DATE_FORMAT)

        end_date = str(raw_input("Please specify a end date in the form [DD-MM-YYYY]. " \
                                 "Tweets after this date will not be queried.\n" \
                                 "Type [now] to query everything up to the current day: "))

        # If the end date is "now", get the current dattim.
        if (end_date == "now"):
            end_date_obj = datetime.now() 
        else:
            end_date_obj = datetime.strptime(end_date, DATE_FORMAT)

        print("If you continue, every tweet between {0} and {1} will be selected.".format(
              start_date_obj.strftime(DATE_FORMAT), end_date_obj.strftime(DATE_FORMAT)))
        confirmed = str(raw_input("Continue? (type yes/no): "))
        if (confirmed == "yes" or confirmed == "Yes"):
            statuses = api.GetUserTimeline(count=200)
            if (sel == "dh"):
                fname = "history_{0}_{1}.txt".format(start_date_obj.strftime(DATE_FORMAT),
                        end_date_obj.strftime(DATE_FORMAT))
                outf = open(fname, "a")

            latest_id = "" 
            i = 1
            deleted = 0
            while len(statuses) > 1:
                for status in statuses:
                    creat_dattim = datetime.fromtimestamp(status.created_at_in_seconds).strftime(DATE_FORMAT)
                    creat_dattim_obj = datetime.strptime(creat_dattim, DATE_FORMAT)
                    if (sel == "dh"):
                        outf.write("{s_id};{s_t};{s_txt}\n".format(s_id = status.id,
                                   s_t = time.asctime(time.gmtime(status.created_at_in_seconds)), 
                                   s_txt = status.text.encode("utf-8")))
                    i += 1
                    latest_id = status.id
                    if ((sel == "dh" or sel == "d") 
                    and (creat_dattim_obj >= start_date_obj and creat_dattim_obj < end_date_obj)): 
                        print(i, status.id, creat_dattim, "destroy=YES") 
                        api.DestroyStatus(latest_id)
                        deleted += 1
                    else:
                        print(i, status.id, creat_dattim, "destroy=NO") 

                statuses = api.GetUserTimeline(count = 200, max_id = latest_id)
            print("Finished. {0} tweets deleted.".format(deleted))
        else:
            print("Aborted.")
else:
    print("nay")
