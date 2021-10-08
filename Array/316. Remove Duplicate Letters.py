316. Remove Duplicate Letters

# 改版单调栈
# 逐个遍历，维护单调栈，除非是唯一字符
# 遍历到栈中已有元素肯定可以直接抛弃，因为已经是单调栈（分段），不可能增加重复元素来优化结果
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
    	import collections
    	# 记录 s 中每个字符出现的次数，辅助判断
    	remain_dict = collections.Counter(s)
    	stack = []

    	for char in s:
    		# 栈中已有字符直接抛弃，因为已经是目前最优解
    		if not char in stack:
    			# 维持单调栈，除非该字符已经是最后一次出现
    			while stack and char < stack[-1] and remain_dict[stack[-1]] > 0:
    				stack.pop()
    			stack.append(char)
    		remain_dict[char] -= 1

    	return ''.join(stack)


# 优化 char in stack 部分

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        import collections
        # 记录 s 中每个字符出现的次数，辅助判断
        remain_dict = collections.Counter(s)
        stack = []
        ##
        stack_set = set()

        for char in s:
            # 栈中已有字符直接抛弃，因为已经是目前最优解
            if not char in stack_set:
                # 维持单调栈，除非该字符已经是最后一次出现
                while stack and char < stack[-1] and remain_dict[stack[-1]] > 0:
                    stack_set.discard(stack.pop())
                stack.append(char)
                stack_set.add(char)
            remain_dict[char] -= 1

        return ''.join(stack)