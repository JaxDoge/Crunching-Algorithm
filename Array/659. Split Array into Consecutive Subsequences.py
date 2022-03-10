#  Greedy algorithm
#  freq records the rest counts of each number, need records the possible position counts of certain number
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        from collections import defaultdict
        freq = defaultdict(int)
        need = defaultdict(int)

        for e in nums:
            freq[e] += 1

        for e in nums:
            if freq[e] == 0:
                continue

            # check the possibility to append e to a subsequence
            if need[e] > 0:
                freq[e] -= 1
                need[e] -= 1
                need[e + 1] += 1
            # otherwise check the possibility to set e as the start of a subsequence
            elif freq[e] > 0 and freq[e + 1] > 0 and freq[e + 2] > 0:
                freq[e] -= 1
                freq[e + 1] -= 1
                freq[e + 2] -= 1
                need[e + 3] += 1
            # or there is a outcast
            else:
                return False

        return True
