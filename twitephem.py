#!/usr/bin/python

# Twitephem 
import twitter
import json
import time
import sys, getopt
from datetime import datetime

from _api import api_key, api_secret, acc_token, acc_secret

VERSION = "1.0"
DATE_FORMAT = '%d-%m-%Y'
global silent
silent = False

def main(argv):
    global silent
    opcode = "v"
    b_date = ""
    e_date = ""
    # Command line arguments
    try:
        opts, args = getopt.getopt(argv, "adhsvb:e:",["archive","delete","help","silent","view","begin=","end="])
    except getopt.GetoptError:
        print("twitephem.py [-hdvasbe]")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("twitephem.py [-hdvasbe]")
            print("     -h:                 Help dialog")
            print("     -s:                 Silent mode (no output / prompts)")
            print("     -d:                 Delete")
            print("     -a:                 Delete and archive history")
            print("     -v:                 View tweets")
            print("     -b <DD-MM-YYYY>     Begin date")
            print("     -e <DD-MM-YYYY>     End date")
            sys.exit()
        elif opt in ("-d", "--delete"):
            opcode = "d"
        elif opt in ("-a", "--archive"):
            opcode = "a"
        elif opt in ("-v", "--view"):
            opcode = "v"
        if opt in ("-b", "--begin"):
            b_date = arg
        if opt in ("-e", "--end"):
            e_date = arg
        if opt in ("-s", "--silent"):
            silent = True

    cprint("TWITEPHEM v%s" % VERSION)
    cprint("Connecting to twitter API.")
    api = twitter.Api(consumer_key=api_key,
                    consumer_secret=api_secret,
                    access_token_key=acc_token,
                    access_token_secret=acc_secret)

    if api:
        cprint("Authentication successful.")
        cprint("Options: d       - Delete tweets")
        cprint("         dh      - Delete tweets & save history")
        cprint("         v       - View tweets")
        sel = "v"
        if not silent:
            sel = str(raw_input("Enter your selection and press enter: "))
        else:
            sel = opcode
        
        if(sel == "d" or sel == "a" or sel == "v"):
            if not silent:
                start_date = str(raw_input("Please specify a start date in the form [DD-MM-YYYY]. " \
                                    "Tweets after this date will be queried: "))
                start_date_obj = datetime.strptime(start_date, DATE_FORMAT)
            elif not b_date == "":
                start_date_obj = datetime.strptime(b_date, DATE_FORMAT)
            else:
                print("Faulty begin date. Aborting.")
                sys.exit()

            if not silent:    
                end_date = str(raw_input("Please specify a end date in the form [DD-MM-YYYY]. " \
                                    "Tweets after this date will not be queried.\n" \
                                    "Type [now] to query everything up to the current day: "))

                # If the end date is "now", get the current dattim.
                if (end_date == "now"):
                    end_date_obj = datetime.now() 
                else:
                    end_date_obj = datetime.strptime(end_date, DATE_FORMAT)
            elif not e_date == "":
                end_date_obj = datetime.strptime(e_date, DATE_FORMAT)
            else:
                print("Faulty end date. Aborting.")

            cprint("If you continue, every tweet between {0} and {1} will be selected.".format(
                start_date_obj.strftime(DATE_FORMAT), end_date_obj.strftime(DATE_FORMAT)))
            
            if not silent: 
                confirmed = str(raw_input("Continue? (type yes/no): "))
            else:
                confirmed = "yes"

            if (confirmed == "yes" or confirmed == "Yes"):
                statuses = api.GetUserTimeline(count=200)
                if (sel == "a"):
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
                        latest_id = status.id
                        if (creat_dattim_obj >= start_date_obj and creat_dattim_obj < end_date_obj): 
                            if (sel == "d" or sel == "a"): 
                                if (sel == "a"):
                                    outf.write("{s_id};{s_t};{s_txt}\n".format(s_id = status.id,
                                    s_t = time.asctime(time.gmtime(status.created_at_in_seconds)), 
                                    s_txt = status.text.encode("utf-8")))
                                    
                                print("{0}, {1}, {2}, {3}".format(i, status.id, creat_dattim, "destroy=YES"))
                                api.DestroyStatus(latest_id)
                                deleted += 1
                            else:
                                print("{0}, {1}, {2}, {3}".format(i, status.id, creat_dattim, "destroy=NO"))
                        i += 1

                    statuses = api.GetUserTimeline(count = 200, max_id = latest_id)
                print("Finished. {0} tweets deleted.".format(deleted))
            else:
                cprint("Aborted.")
    else:
        cprint("Connection failed. Check data in _api.py")

def cprint(a):
    global silent
    if silent == False:
        print(a)

if __name__ == "__main__":
    main(sys.argv[1:])
