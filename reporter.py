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

    #Sol 
    parser.add_argument(
        "sol", nargs="?", type=int, help="Mars' Sol Number" 
    )

    #atmospheric temperature 
    parser.add_argument(
        "atmospheric_temperature", 
        nargs="?", 
        help="Atmospheric temperature of the day."
    )

    #horizontal wind speed
    parser.add_argument(
        "-hws",
        "--horizontal_wind_speed",
        action="store_true",
        help="display the horizontal wind speed."
    )

    #atmospheric pressure
    parser.add_argument(
        "-pre",
        "--atmospheric_pressure", 
        action="store_true",
        help="display the atmospheric pressure."
    )

    #wind direction
    parser.add_argument(
        "-wd",
        "--wind_direction",
        action="store_true",
        help="display the horizontal wind speed."
    )


    return parser.parse_args

def building_url():
    #Call API key
    api_key = get_api_key()

    #Buiding the url
    url = (f"//api.nasa.gov/insight_weather/?api_key={api_key}&feedtype=json&ver=1.0")

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
        return json.loads(data) 
    except:
        sys.exit("Couldn't read the server response.")
    

def display_information(data, sol, atmospheric_temperature=True, horizontal_wind_speed=False, atmospheric_pressure=False, wind_direction=False):
    # Check if the sol is in the data
    if str(sol) in data:
        sol_data = data[str(sol)]
        
        # Display atmospheric temperature
        if atmospheric_temperature and 'AT' in sol_data:
            print(f"Sol {sol} average temperature: {sol_data['AT']['av']} degrees Celsius")
        
        # Display horizontal wind speed
        if horizontal_wind_speed and 'HWS' in sol_data:
            print(f"Sol {sol} average horizontal wind speed: {sol_data['HWS']['av']} m/s")
        
        # Display atmospheric pressure
        if atmospheric_pressure and 'PRE' in sol_data:
            print(f"Sol {sol} average atmospheric pressure: {sol_data['PRE']['av']} Pa")
        
        # Display wind direction
        if wind_direction and 'WD' in sol_data:
            most_common_direction = max(sol_data['WD'], key=lambda x: x['compass_degrees'])
            print(f"Sol {sol} most common wind direction: {most_common_direction['compass_point']} ({most_common_direction['compass_degrees']} degrees)")
    else:
        print(f"No data available for Sol {sol}")

    

if __name__ == "__main__":
    user_args = read_user_arguments()
    query_url = building_url()
    data_from_url = get_data_from_url(query_url)
