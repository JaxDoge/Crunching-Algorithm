380. Insert Delete GetRandom O(1)


class RandomizedSet:

    def __init__(self):
    	self.number_list = list()
    	# value is unique
    	# facilitate moving the to-be-remove int to the tail of list
    	self.val_to_index = dict()


    def insert(self, val: int) -> bool:
    	if val in self.val_to_index:
    		return False
    	self.val_to_index[val] = len(self.number_list)
    	self.number_list.append(val)
    	return True


    def remove(self, val: int) -> bool:
    	if not val in self.val_to_index:
    		return False
    	index = self.val_to_index[val]
    	last_val = self.number_list[-1]
    	# 和最后一个元素交换位置
    	self.number_list[index], self.number_list[-1] = self.number_list[-1], self.number_list[index]
    	# VI 字典也要修改
    	self.val_to_index[last_val] = index
    	del self.val_to_index[val]
    	self.number_list.pop()
    	return True

    def getRandom(self) -> int:
    	import random
    	return self.number_list[random.randrange(len(self.number_list))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()