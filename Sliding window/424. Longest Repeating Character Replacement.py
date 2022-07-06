424. Longest Repeating Character Replacement



# sliding window
# try to extend the right end of the window
# the characters in the windows fit into two categories
# 1. the majority, if there is no "the" majority, choose one arbitrarily
# 2. the minority, their appearances cannnot exceed number k
class Solution:
    def convert(self, ch):
        return ord(ch) - ord("A")

    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n < 2:
            return 1

        counter = [0] * n
        left = right = 0
        counter[self.convert(s[0])] += 1
        majority = s[0]

        while right < n - 1:
            # move right pointer forward
            right += 1

            # add new character into counter
            counter[self.convert(s[right])] += 1

            # check if the majority need update
            if counter[self.convert(majority)] < counter[self.convert(s[right])]:
                majority = s[right]

            # if the sum of minority is larger than k (because of moving right pointer)
            # dwindle the window size by moving left pointer
            # as a result, the window size stay as the last round
            if sum(counter) - counter[self.convert(majority)] > k:

                counter[self.convert(s[left])] -= 1
                left += 1


        return right - left + 1





