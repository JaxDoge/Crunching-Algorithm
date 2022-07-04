剑指 Offer 50. 第一个只出现一次的字符


# we use queue to maintain the the first unique character
# we use a hashmap to record each character and its duplication
# the first time we encount a character, record its position; the second time we find it, change the value to -1
# every time we change a value to -1, check the first element in the queue if it should be popped
# maybe there are some character in the middle of the queue should be popped, but we only have to maintain the first on
# is the unique character
class Solution:
    def firstUniqChar(self, s: str) -> str:
        from collections import deque
        counter = dict()
        q = deque()

        for idx, ch in enumerate(s):
            if ch not in counter:
                counter[ch] = idx
                q.append(ch)
            else:
                counter[ch] = -1
                while q and counter[q[0]] == -1:
                    q.popleft()

        return " " if not q else q[0]

