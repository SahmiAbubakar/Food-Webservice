import requests
import json
class GeocodioClient(object):
    """
    The client that makes request to the Geocodio 
    to get the corresponding (latitude, longitude) pair. 
    """
    def __init__(self, api_key):
        # implement your code here.
        # store the necessary information of the client.
        self.api_key = api_key
        pass

    def request(self, addr):
        # implement your code here.
        # in addr, we use the dash '-' to replace the space ' ' in the address. 
        # make sure you parse the address correctly.
        # returns the (latitude, longitude) pair.
        
        self.addr = addr.replace(" ","-")
        
        q = self.addr
        apiKey = self.api_key
        request = "https://api.geocod.io/v1.6/geocode?q="+q+"&api_key="+apiKey
        r = requests.get(request)

        APISTATUS = r.status_code
        if APISTATUS == 200:
            jsoninfo = r.json()

            results = jsoninfo.get('results')
            if(results == []):
                return "GEOCODE API ERROR", "GEOCODE API ERROR"
            location = results[0].get('location')
            
            #data = json.load(r)
            latitude = location.get('lat')
            longitude = location.get('lng')
            return latitude, longitude
        else:
            return "GEOCODE API ERROR", "GEOCODE API ERROR"
            pass


class YelpClient(object):
    """
    The client that makes request to the Yelp
    to get a list of nearby restaurants.
    """
    def __init__(self, api_key):
        # implement your code here.
        # store the necessary information of the client.

        self.api_key = api_key

        pass

    def request(self, latitude, longitude):
        # implement your code here.
        # don't forget to transform the raw returned value to our desired form.
        self.latitude = latitude
        self.longitude =longitude
        headers = {
            "accept": "application/json",
            "Authorization":self.api_key
        }
        request = "https://api.yelp.com/v3/businesses/search?latitude="+str(latitude)+"&longitude=" + str(longitude)+"&categories=Food&sort_by=best_match&limit=20"
        r = requests.get(request, headers=headers, timeout=30)
        APISTATUS = r.status_code
        if APISTATUS == 200:
            jsoninfo = r.json()
            
            totalBusinesses = jsoninfo.get('businesses')
            list = []
            for business in totalBusinesses:
                tempdict = {}
                Name = business.get('name')
                location = business.get('location')
                address = location.get("display_address")[0]+ " " + location.get("display_address")[1]
                rating = business.get('rating')
                tempdict["name"] = Name
                tempdict["address"] = address
                tempdict["rating"] = rating
                list.append(tempdict)
            dictionary = {"restaurants": list}

            return dictionary 
        else:
            return "YELP API ERROR"
            pass

