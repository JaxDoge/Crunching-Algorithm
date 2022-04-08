14. Longest Common Prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        i = 0
        j = 0
        checker = list()
        ans = list()
        while True:
            if strs[i] == "" or j >= len(strs[i]):
                break
            if i == 0 or strs[i][j] == checker[0]:
                checker.append(strs[i][j])
                i += 1
            else:
                break

            if len(checker) == n:
                ans.append(checker[0])
                i = 0
                j += 1
                checker = list()

        return ''.join(ans)




