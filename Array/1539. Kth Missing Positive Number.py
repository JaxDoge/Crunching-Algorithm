1539. Kth Missing Positive Number




class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        p = 0
        ans = 1
        n = len(arr)

        while True:
            # if ans is not missing
            if p < n and arr[p] == ans:
                p += 1
                ans += 1

            else:
                k -= 1
                if k == 0:
                    break
                ans += 1

        return ans