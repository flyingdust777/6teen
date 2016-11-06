# Combines multiple functions to return a sorted large list made up of objects and their ranking (sorted according to ranking)
# Returns bigList = [[business_object0, ranking], [business_object1, ranking]...]
from models import business
def function_combine():
	lat_long = ip_location() #get lat and long from ip_location function
	#need to get activity
	search_results = yelp_query(lat_long)	#get all search results from yelp via yelp_query function (should return a rather large object)
	cut_search_results = []
	businessClass = business()
	for int in search_results.total:
		businessClass.name  = search_results.businesses[i].name
		businessClass.yelp_rate = search_results.businesses[i].rating
		businessClass.app_rate = 0
		businessClass.latitude = search_results.businesses[i].location.coordinate.latitude
		businessClass.longitude = search_results.businesses[i].location.coordinate.longitude
		#cut search results are a list of lists that have 4 terms: name, yelp rating, our rating, address
		cut_search_results.append([search_results.businesses[i].name, search_results.businesses[i].rating, dank_algo(user1, search_results.businesses[int]), search_results.businesses[i].location.cross_streets])
	bigList = []
	user1 = 
	for int in search_results.total:	#for every business, make a sub-list called rankList which contains that business info, and the ranking. Append this to bigList
		businessClass.app_rate = cut_search_results[i][2]
		rankList = [search_result.business[int], dank_algo(user1, businessClass)]
		bigList.append(rankList)
	bigList = sort_rank(bigList)	#sort the bigList according to the rankings
	return bigList
