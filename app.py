from flask import Flask
from flask import request

import argparse
import requests
import json

from clients import GeocodioClient, YelpClient

app = Flask(__name__)

# ENTER API KEY HERE
API_KEY = ""
YELP_API = "Bearer "

@app.route('/restaurants', methods=['GET'])
def rest():
    if request.method == 'GET':
        return "200-OK"
        pass
    else:
        return "error"
@app.route('/restaurant/', methods=['GET'])
def Fail():
    if request.method == 'GET':
        return "ERROR: Enter a Location to view restaurants nearby.", 400
        pass
    else:
        return "error"

@app.route('/restaurant/<restaurant_addr>', methods=['GET'])
def restaurant(restaurant_addr):
    if request.method == 'GET':
        # Implement your function here.

        GeoClient = GeocodioClient(API_KEY)
        lat, long = GeoClient.request(restaurant_addr)
        if lat != "GEOCODE API ERROR":
            YClient= YelpClient(YELP_API)
            dictionary = YClient.request(lat,long)
            json_object = json.dumps(dictionary, indent=4)
            if json_object != '"YELP API ERROR"':
                return json_object
            else:
                json_object = "YELP API ERROR"
                return json_object, 500
        else:
            json_object = "GEOCODE API ERROR"

        return json_object, 500
        pass
    else:
        # Implement your function to deal with false requests.
        return "Enter A Valid Request", 500
        pass

##########################
# Do **NOT** remove this.
def parse_args():
    parser =argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000,
                        help='port number.')
    return parser.parse_args()

if __name__ == '__main__': 
    args = parse_args()
    app.run(port=args.port)