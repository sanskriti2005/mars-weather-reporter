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

    try:
        #initializing http request from the request object
        response = request.urlopen(req)
    #incase of an error
    except error.HTTPError as http_error:
        # 401 Unauthorized
        if http_error.code == 401:
            sys.exit("Access Denied, Check you API key.")
        # 404 Not-found
        elif http_error.code == 404:
            sys.exit("Can't find the data/ the data is not available due to problems in, out aplogies.")
        else:
            sys.exit(f"Something went wrong... ({http_error.code})")


    #data from the response is read
    data = response.read()

    #returns deserialized json data
    try:
        return.json.loads(data) 
    except:
        sys.exit("Couldn't read the server response.")
    

def display_information(arg1, arg2=False, arg3=False):
    print(f"Temp:{}")

    if arg2:
        print(f"")
    if arg3:
        print(f"")
    