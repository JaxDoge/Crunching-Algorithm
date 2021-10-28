787. Cheapest Flights Within K Stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    	# the largest edge number the path takes is k + 1
    	k = k+1

    	# record the previous stations of every destination
    	import collections
    	destination_dict = collections.defaultdict(list)
    	for f in flights:
    		from_ = f[0]
    		to_ = f[1]
    		price_ = f[2]
    		destination_dict[to_].append([from_, price_])

    	