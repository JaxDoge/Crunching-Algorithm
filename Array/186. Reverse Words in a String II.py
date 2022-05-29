186. Reverse Words in a String II



# Total reverse
# Then part reverse

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        if n == 1:
            return

        s.reverse()
        start = 0
        end = 0

        def rev(i, j):
            nonlocal s
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

            return

        while start < n:
            # move end to the end of each word
            while end < n and s[end] != " ":
                end += 1

            # reverse
            rev(start, end - 1)
            end += 1
            start = end



        return
