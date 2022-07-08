395. Longest Substring with At Least K Repeating Characters


# findout all "separator" letters
# divide and conquer
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def convert(ch):
            return ord(ch) - ord("a")

        def dfs(left, right):
            nonlocal s, k

            counter = [0] * 26
            # go through the target string from left to right
            for i in range(left, right + 1):
                counter[convert(s[i])] += 1


            split = "#"
            # find a separator
            for i in range(len(counter)):
                if 0 < counter[i] < k:
                    split = chr(ord("a") + i)
                    break

            # if there is no separator within this segment, the length of this segment is valid substring
            if split == "#":
                return right - left + 1


            # continue segment the string, via locating the start and end points of each one
            # using a pointer to go through the string and locate the start and end points of each segment
            p = left
            res = 0
            while p <= right:
                # moving p toward if p at a separator letter
                while p <= right and s[p] == split:
                    p += 1  

                # p could be move out at this point
                if p > right:
                    break

                start = p
                # find the end point, p will point to the first separator from start point, or just at right + 1
                while p <= right and s[p] != split:
                    p += 1
                tmp = dfs(start, p - 1)
                res = max(res, tmp)

            return res

        return dfs(0, len(s) - 1)




