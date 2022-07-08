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



# Or we could still use sliding windows
# The tricky is, the candidate substring can only contain [1~26] different letters
# so we could add a extra constrain on each seach iteration
# The number of distinct letters
# and do such sort of search 26 times
# It is unnecessary loop 26 times, considering the s may contain less distinct letters

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        counter = [0] * 26
        ans = 0

        for c in s:
            idx = ord(c) - ord("a")
            if counter[idx] == 0:
                counter[idx] += 1

        maxLetter = sum(counter)

        for maxL in range(1, maxLetter + 1):
            count = [0] * 26
            left = right = 0
            inLetter = 0
            validL = 0
            while right < n:
                curL = s[right]
                idx = ord(curL) - ord("a")
                count[idx] += 1

                # if the cnt of curL is 1, in-window letter += 1
                if count[idx] == 1:
                    inLetter += 1
                # if the cnt of curL is k, then validL += 1
                if count[idx] == k:
                    validL += 1

                # move left end base on the inequation maxL > inLetter
                while inLetter > maxL:
                    rightIdx = ord(s[left]) - ord("a")
                    if count[rightIdx] == 1:
                        inLetter -= 1
                    if count[rightIdx] == k:
                        validL -= 1   
                    count[rightIdx] -= 1

                    left += 1

                # if validL == inLetter, the substring in the window is one of potential answer
                if validL == inLetter:
                    ans = max(ans, right - left + 1)

                right += 1


        return ans