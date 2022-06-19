剑指 Offer 48. 最长不含重复字符的子字符串

# Double pointers
# Slide window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        memo = set()

        right = -1
        for left in range(n):
            # each time, we move left ahead, remove the element in left - 1 from memo set
            if left != 0:
                memo.remove(s[left - 1])

            # if it is possible, move right pointer forward    
            while right + 1 < n and s[right + 1] not in memo:
                memo.add(s[right + 1])
                right += 1

            # update the ans with the length of window
            # note that the elements in the window is distinct
            ans = max(ans, right - left + 1)

        return ans




