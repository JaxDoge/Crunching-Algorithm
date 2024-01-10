14. Longest Common Prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        i = 0
        j = 0
        checker = list()
        ans = list()
        while True:
            # Base case, if any string is empty or the shortest string is shorter than index j, just break the loop 
            if strs[i] == "" or j >= len(strs[i]):
                break

            # if current string is the first one or current index character equal to the previous character in different string, continue
            # Otherwise just break
            if i == 0 or strs[i][j] == checker[0]:
                checker.append(strs[i][j])
                i += 1
            else:
                break

            # All strings are checked on the j index, ready for the next loop
            if len(checker) == n:
                ans.append(checker[0])
                i = 0
                j += 1
                checker = list()

        return ''.join(ans)




