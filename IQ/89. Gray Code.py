89. Gray Code


# Backtrak
from collections import Counter
class Solution:
    def grayCode(self, n: int) -> List[int]:
        memo = {0}  # record picked num in ten digits
        res = [0]
        

        def backtrack():
            nonlocal memo, res, n
            # base case, when the length of res is n and the last element is valid
            if len(res) == 2 ** n:
                htXOR = res[0] ^ res[-1]
                counter = Counter("{0:b}".format(htXOR))
                if counter["1"] == 1:
                    return True

                return False

            flag = False
            for i in range(n):
                medium = "0" * i + "1" + "0" * (n - i - 1)
                cand = res[-1] ^ int(medium, 2)
                if cand not in memo:
                    res.append(cand)
                    memo.add(cand)
                    flag = backtrack()
                    if flag:
                        break
                    res.pop()
                    memo.remove(cand)

            return flag

        backtrack()
        return res



# Formula
# https://baike.baidu.com/item/%E6%A0%BC%E9%9B%B7%E7%A0%81
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0] * (1 << n)
        for i in range(1 << n):
            ans[i] = (i >> 1) ^ i
        return ans

