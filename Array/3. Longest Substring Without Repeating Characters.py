3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        duplicate_num = 0
        p1 = 0
        res = 0

        n = len(s)

        for p2 in range(n):
            # put s[p2] in the subarray
            if hashmap[s[p2]] == 1:
                duplicate_num += 1
            hashmap[s[p2]] += 1

            # if there is at least one duplicate char, stop extending the window
            if duplicate_num > 0:
                if hashmap[s[p1]] == 2:
                    duplicate_num -= 1
                hashmap[s[p1]] -= 1
                p1 += 1
            
            if duplicate_num == 0:
                res = max(res, p2 - p1 + 1)

        return res

