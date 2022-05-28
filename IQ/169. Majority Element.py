169. Majority Element


'''
投票法正确思路：不妨假设整个数组的众数记做a，则最初的数组中a的数量大于其余所有数。当采用count计数的时候有两种情况：

1）假设candidate等于a，则当count从1变为0的过程，此区间内a的数量等于其余数的数量，因此以count=0为分界线，数组右端部分的众数仍然为a

2）假设candidate不等于a，则当count从1变为0的过程， 此区间内a的数量小于等于其余数的数量，因此以count=0为分界线，数组右端部分的众数仍然为a

因此，以count=0可以将整个原始数组分为若干部分，count=0右端部分的数组中的众数永远是a，最终必然会筛选出a
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cand = float("inf")
        count = 0 

        for i in range(n):
            if count == 0:
                cand = nums[i]
            
            if cand == nums[i]:
                count += 1
            else:
                count -= 1

        return cand



# Divide Conquer

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
