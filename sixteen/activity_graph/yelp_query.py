from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import yelp
import io
import json
#read API keys from the json file and initiate autheticator
#launch client
with io.open('config_secret.json') as cred:
 	creds = json.load(cred)
 	auth = Oauth1Authenticator(**creds)
 	client = Client(auth)
# now can use client object to make requests to Yelp
# function takes two arguments, a tuple and string
# returns an object containing list of businesses + other info
def yelp_query(lat_long, activity):
	params = {'term': activity, 'lan': 'en'}
	search_results = client.search_by_coordinates(lat_long[0], lat_long[1], **params)
	return search_results
	## for testing purposes
	# print search_results.total
	# print search_results.businesses[0].categories
	# print search_results.businesses[0].location.city
	# print search_results.businesses[0].name
	# print search_results.businesses[0].rating
	# print search_results.businesses[0].snippet_text