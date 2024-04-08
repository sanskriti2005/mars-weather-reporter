import argparse
import os
from urllib import request, parse, error
import json
import sys

# SET-UP API KEY
def get_api_key():
    return os.getenv("INSIGHT_API_KEY")


# PARSING USER ARGUMENTS 
def read_user_arguments():
    #Argument Parser
    parser = argparse.ArgumentParser(
        description="Reports Mars' current atmospheric temperature"
    )

    parser.add_argument(        #add arguments here

    )


    return parser.parse_args

def building_url():
    api_key = get_api_key()
    url = (
        f"<url>{api_key}<url>"
    )
    return url

def get_data_from_url(url):
    #create a request object for the built url and add a user-agent
    req = request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
    


def display_information(arg1, arg2=False, arg3=False):
    print(f"Temp:{}")

    if arg2:
        print(f"")
    if arg3:
        print(f"")
    