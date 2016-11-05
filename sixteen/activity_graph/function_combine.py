# Combines multiple functions to return a sorted large list made up of objects and their ranking (sorted according to ranking)
# Returns bigList = [[business_object0, ranking], [business_object1, ranking]...]
def function_combine():
	lat_long = ip_location() #get lat and long from ip_location function
	#need to get activity
	search_results = yelp_query(lat_long, activity)	#get all search results from yelp via yelp_query function (should return a rather large object)
	bigList = []
	for int in search_results.total:	#for every business, make a sub-list called rankList which contains that business info, and the ranking. Append this to bigList
		rankList = [search_result.business[int], dank_algo(user1, search_result.business[int])]
		bigList.append(rankList)
	bigList = sort_rank(bigList)	#sort the bigList according to the rankings
	return bigList
