170. Two Sum III - Data structure design

# Solution 1, improve find function time complexity
class TwoSum:

    def __init__(self):
    	self.sums_set = set()
    	self.nums_list = list()

    def add(self, number: int) -> None:
    	# add new nums, update sums_set
    	for num in self.nums_list:
    		self.sums_set.add(num+number)
    	self.nums_list.append(number)


    def find(self, value: int) -> bool:
    	if value in self.sums_set:
    		return True
    	return False


# Solution 2, standard

class TwoSum:

    def __init__(self):
    	from collections import defaultdict
    	self.num_freq = defaultdict(int)

    def add(self, number: int) -> None:
    	# add new nums, update sums_set
    	self.num_freq[number] += 1


    def find(self, value: int) -> bool:
    	for key in self.num_freq:
    		rest = value - key
    		if rest != key and rest in self.num_freq:
    			return True
    		elif rest == key and self.num_freq[rest] > 1:
    			return True
    	return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)