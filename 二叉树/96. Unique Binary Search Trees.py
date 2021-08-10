96. Unique Binary Search Trees


# 在递归框架下，注意一个细节，我们不在意每个子序列的具体的值，而是序列本身的长度
# 那么在分治思想下，以 i 为根节点的左子树组合对应序列为[1,2,...,i-1], 右子树组合对应序列 [1,2,...,n-i]
# 这样就不需要记录 low & high，而是每个子序列的长度即可，从而节约备忘录的空间使用


class Solution:
    def numTrees(self, n: int) -> int:
        import collections
    	memo = collections.defaultdict(int)
    	def counter(n: int):
    		nonlocal memo
    		if n <= 1:   # Only one or None node, there is one result
    		    return 1
            
            res = 0
    		for i in range(1,n+1):
    			# Check the memo if the left subtree counter exists
    			if memo[i-1]:
    				left_num = memo[i-1]
    			else:   #  Has previous result, read it
    				left_num = counter(i-1)
    				memo[i-1] = left_num

    			# Same the memo if the left subtree counter exists
    			if memo[n-i]:
    				right_num = memo[n-i]
    			else:

					right_num = counter(n-i)
    				memo[n-i] = right_num

    		    res += left_num * right_num
            return res 

        return counter(n)




# 卡塔兰级数，没什么可说的，背公式吧

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)

