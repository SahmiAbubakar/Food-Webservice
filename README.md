# Food-Webservice
In this project, it was seen that we can send address data from a client to the foodie server
via the use of HTTP 1.1 protocol. This data is then routed to another endpoint (Geocodio), via
the same protocol, and returns information back to the foodie web service endpoint with the use
of a GET request. This information is then used by the Foodie web service to send a GET request
to the Yelp endpoint. The yelp endpoint returns up to 20 different popular food locations in the
vicinity of the address that was originally entered. In this project, the client is only
communicating with the foodie server, and the foodie server is communicating with the client,
Geocodio, and with Yelp. Upon a successful GET request from a client to the foodie server, the
server sends a 200 response with information of all the nearby food locations. It was also
important to handle errors in this lab. For example, if a client were to enter an endpoint of
/restaurant/, the server would return a response of 400, with the string “ERROR: Enter a
Location to view restaurants nearby.” as the client did not format the GET request as
needed. If the Geocodeio API, or the Yelp API were was to fail, the foodie server would return
an error message with a status code of 500, and a string of “GEOCODE API ERROR'' or “YELP
API ERROR” depending on which api fails. This was achieved by taking the status of the
response that the foodie web service endpoint received from the GET requests from the different
API’s. Anything other than a response of 200 from the Yelp API or the Geocodio API would
result in the foodie web service to see a bad request, meaning that the client would receive a 500
response. 500 means “INTERNAL SERVER ERROR”, meaning that the server had an issue
handling the request. This includes having a bad address with correct request syntax, having the
Geocode API fail, or having the Yelp API fail. The client also has to have the proper syntax of
the request. Having /restaurant/<address> where the address value is a string separated by either
spaces or dashes will result in a 200 status, unless the address is gibberish resulting in a 500
status code.
This project also shows how we can use distributed systems in order to achieve a goal. In
this case, the distributed systems were the foodie web service, the geocode api, and the yelp
service. We were able to see how to handle errors in communicating between the different
endpoints, and how these errors can be displayed to the client in a fashion such that the client is
able to decipher what happened. Students were also able to understand how the HTTP 1.1 GET
method works, which is that it sends a request to an endpoint via the header parameters, and
receives information in the body of the response, along with a status code.
Some issues that I had encountered were figuring out how to handle a null address
request, and return a proper status code of 400, with text saying that there is no address input in
the GET method. In order to do this, I created another endpoint “/restaurant/”. This endpoint
returned a status code of 400, with a message saying “ERROR: Enter a Location to view
restaurants nearby.”. Another issue I had encountered was handling the way that the
Foodie web service was to handle Yelp and Geocodio errors. In order to resolve this issue, I
viewed the status of the get requests sent by the Foodie web service, and then based on this status
code, the foodie web server would decide whether the client would receive a 500 or a 200 code.
In this project the libraries & packages used were Flask, JSON, requests, and argparse. Flask was
used to create the GET request, JSON was used to format the data retrieved from Yelp, requests
were used to send and view information about HTTP GET requests sent to Yelp, and to
Geocodio, and argparse was used to parse the request sent to the Foodie server.
To start the web service, run app.py, and in postman type the
host:port/restaurants/address(separated by spaces). In curl type curl
host:port/restaurant/address(separated by dashes)
In this project, the Geocod.io / Yelp API keys were placed in app.py on lines 13 and 14.
*note Bearer needs to be present in order for the yelp API key to function properly.*
