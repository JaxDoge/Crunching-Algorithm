564. Find the Closest Palindrome




# https://leetcode.cn/problems/find-the-closest-palindrome/solution/xun-zhao-zui-jin-de-hui-wen-shu-by-leetc-biyt/
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        #一共五种情况 12345
        # 1）前面的一半放到后面     -> 12321
        # 2）前面的一半加1放到后面  -> 12421
        # 3）前面的一半减1放到后面  -> 12221
        # 4）上边界   -> 100001
        # 5）下边界   -> 9999

        m = len(n)        

        if m == 1:
            return str(int(n) - 1)

        # substring the pre-half string, if m is odd, the middle number is included
        headSeg = n[:m//2 + m%2]
        minusOne = str(int(headSeg) - 1)
        addOne = str(int(headSeg) + 1)

        cand = [
            "9" * (m - 1),
            "1" + "0" * (m - 1) + "1",
            headSeg + headSeg[(m//2 - 1)::-1],
            minusOne + minusOne[(m // 2 - 1)::-1],
            addOne + addOne[(m // 2 - 1)::-1]
        ]

        return min(cand, key = lambda x: (abs(int(n) - int(x)) or int(n), int(x)))