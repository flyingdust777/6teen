# takes an unsorted list with sublists and sorts them based on the second element in the sub-list
# returns the sorted list
def sort_rank(unsorted_list):
	unsorted_list.sort(key=lambda x: x[1]) #lambda is the 2nd element, and .sort sorts based off that
	return unsorted_list