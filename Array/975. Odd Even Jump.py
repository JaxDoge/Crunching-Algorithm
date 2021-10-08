975. Odd Even Jump


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
    	N = len(arr)

    	# 计算每个 index 的奇数/偶数 跳跃的下一个索引，
        def make(B):
            ans = [None] * N
            # 为啥是递减栈，因为跳跃的条件是 i < j, 那么保持递减栈，弹出的时候是栈顶的索引遇到第一个大于它的索引
            stack = []  # invariant: stack is decreasing
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        # B 是按递增（递减）顺序排列的 A 的 index，排序依据是 arr[i]
        B = sorted(range(N), key = lambda i: arr[i])
        oddnext = make(B) # 奇数跳下一个索引
        B.sort(key = lambda i: -arr[i])
        evennext = make(B) # 偶数跳下一个索引

        # 某个索引在奇数跳（偶数跳）的情况下是否是 good index
        odd = [False] * N
        even = [False] * N

        # 最后一个索引必然是 good index
        odd[N-1] = even[N-1] = True

        # 动态规划部分，从后往前更新状态
        for i in range(N-2, -1, -1):
        	# 如果当前索引有合法奇数跳，则是否是 good index 取决于下个落地索引的偶数跳是否 good index
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            # 偶数同理，
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        return sum(odd)
