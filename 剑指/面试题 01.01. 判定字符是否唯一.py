面试题 01.01. 判定字符是否唯一



# Hashmap

class Solution:
    def isUnique(self, astr: str) -> bool:
        from collections import defaultdict
        memo = defaultdict(int)

        for c in astr:
            memo[c] += 1
            if memo[c] == 2:
                return False

        return True