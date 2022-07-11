557. Reverse Words in a String III


# Two pointers
class Solution:
    def reverseWords(self, s: str) -> str:
        sList = list(s)
        n = len(s)

        left = right = 0

        while right < n:
            while right < n and sList[right] != ' ':
                right += 1
            
            end = right - 1
            while left < end:
                sList[left], sList[end] = sList[end], sList[left]
                left += 1
                end -= 1
            
            right += 1
            left = right 
        
        return "".join(sList)