2024. Maximize the Confusion of an Exam



# sliding window
# find the majority
# count the minority
# remember if the window is invalid, we could only move left end forward once, because even the next window
# is still invalid, the final ans would not be affected. Or the window size would not go down
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        if k == n:
            return n

        if n < 2:
            return 1

        left = right = 0
        counter = [0, 0]
        ans = 0
        # majority = answerKey[0]
        majN = 0
        while right < n:
            if answerKey[right] == "T":
                counter[0] += 1
            else:
                counter[1] += 1

            # update the number of majority letter
            majN = max(counter)

            # if the rest letters' count is larger than k, then move the left end
            if right - left + 1 - majN > k:
                if answerKey[left] == "T":
                    counter[0] -= 1
                else:
                    counter[1] -= 1
                left += 1

            right += 1

        # right point to n index
        return right - left + 1 - 1