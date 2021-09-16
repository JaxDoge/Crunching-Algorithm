277. Find the Celebrity

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# 逆向思维，判断谁是名人很麻烦，但判断谁不是名人非常简单，把不是名人的人都排除，检查最后剩下的是否是名人即可
# 从第一个人开始作为名人候选，用他来排除 others ，或者被排除，被 others 代替候选位置
class Solution:
    def findCelebrity(self, n: int) -> int:
    	cand = 0
    	for i in range(n):
    		if knows(cand,i) or not knows(i,cand):
    			#如果 cand 知道别人，或者别人不知道 cand，抛弃 cand
    			cand = i  
    		else:
    			# 其他三种情况均可以选择抛弃 others，其实有两种情况 cand 和 others 都可以抛弃，但这点没有优化价值
    			pass 

    	# 检查最后的 cand 是否是真实名人
    	for i in range(n):
    		# Bad case, celebrity knows herself/hiself
            if i == cand: continue  
    		if knows(cand, i) or not knows(i, cand):
    			return -1

    	return cand

