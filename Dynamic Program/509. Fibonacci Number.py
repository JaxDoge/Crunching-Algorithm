509. Fibonacci Number

# dp table
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        dp_table = [0] * (n+1)
        dp_table[0] = 0
        dp_table[1] = 1

        for i in range(2, n+1):
            dp_table[i] = dp_table[i-2]+dp_table[i-1]
        return dp_table[n]



# compress space complexity
class Solution:
    def fib(self, n: int) -> int:
    	if n == 0:
    		return 0
    	if n == 1:
    		return 1

    	last_1 = 0
    	last_2 = 1
    	for i in range(2,n+1):
    		curr = last_1 + last_2
    		last_1 = last_2
    		last_2 = curr
    	return curr



