# Twitephem
---
## A tweet manipulation tool
Written in python, using the [Python-Twitter](https://python-twitter.readthedocs.io/en/latest/installation.html) API, this tool allows you to manipulate your own tweets from the command line. Can be executed periodically to generate an ephemeral twitter account.

## Installation
    pip install python-twitter

## Disclaimer
This was a fun project created with little error handling on an afternoon. Use at your own discretion.
I am not responsible for broken Twitter accounts :)

## Usage
Place your own Twitter API key in the api.py file and rename it to \_api.py 
Make sure to keep the file in the .gitignore and manage the permissions properly.
    
### Normal start:

    python twitephem.py

### Silent start:
This is mostly for automatic execution on a fixed schedule, to generate a truly ephemeral Twitter experience.

    python twitephem.py --silent -a -b <DD-MM-YYYY> -e <DD-MM-YYYY>

To make proper use out of this, I've included a shell script where you can specify the longevity of your tweets by specifying how many years, weeks, days should be kept untouched.

    # Delete everything but the last 2 weeks.
    ./autoTwitEphem.sh -w 2    
    # Delete everything but the last year.
    ./autoTwitEphem.sh -y 1
    # Delete everything but the last year and 3 weeks and 5 days.
    ./autoTwitEphem.sh -y 1 -w 3 -d 5

I recommend piping the output to a logfile, so you can refer to it later. The script will always use the **archive** option, so it will automatically create a history file and delete afterwards. You can change that behaviour by editing the script.

### Help:
A list of all possible arguments can be viewed by calling:

    python twitephem.py -h

