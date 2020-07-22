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
    
Normal start:
    python twitephem.py

Silent start:
This is mostly for automatic execution on a fixed schedule, to generate a truly ephemeral Twitter experience.
    python twitephem.py --silent -dh -b <DD-MM-YYYY> -e <DD-MM-YYYY>

A list of all command line arguments is printed on calling:
    python twitephem.py -h

