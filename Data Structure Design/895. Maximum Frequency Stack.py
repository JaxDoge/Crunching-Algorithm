895. Maximum Frequency Stack

class FreqStack:
    def __init__(self):
    	self.maxFreq = 0
    	self.val_freq = dict()
    	self.freq_val = dict()  # value is a stack, which is a list


    def push(self, val: int) -> None:
    	# corresponding CURRENT frequence of this value
    	if not val in self.val_freq:
    		freq = 1
    	else:
    		freq = self.val_freq[val] + 1

    	# update VF dict
    	self.val_freq[val] = freq
    	# update FV dict
    	if not freq in self.freq_val:
    		self.freq_val[freq] = []
    	self.freq_val[freq].append(val)
    	self.maxFreq = max(self.maxFreq, freq)


    def pop(self) -> int:
    	pop_val = self.freq_val[self.maxFreq].pop()
    	# update VF dict
    	self.val_freq[pop_val] = self.maxFreq - 1

    	# update FV dict
    	if not self.freq_val[self.maxFreq]:
    		del self.freq_val[self.maxFreq]
    		self.maxFreq -= 1
    	return pop_val
