159. Longest Substring with At Most Two Distinct Characters


# Sliding Window
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        # sliding the w[l:r+1]
        res = 1  # update res while expand the window
        counter = defaultdict(int)
        counter[s[0]] = 1
        while right < n - 1:
            # expand
            right += 1
            counter[s[right]] += 1

            # Shrinking the window while counter has more than 2 keys
            while len(counter) > 2:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1


            res = max(res, right - left + 1)

        return res

