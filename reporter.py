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
        description="User asks for temperature and gets to know of the temperature in Mars."
    )

    parser.add_argument