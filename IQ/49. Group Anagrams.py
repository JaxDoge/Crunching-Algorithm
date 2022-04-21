49. Group Anagrams



# too damn slow
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        memo = set([])
        n = len(strs)

        for i in range(n):
            if i in memo:
                continue
            word = strs[i]
            # Find the group
            for kw in res.keys():  # Slow!!
                if self.compare(word, kw):
                    res[kw].append(word)
                    memo.add(i)
                    continue
            # Add a new group
            res[word] = [word]

        return list(res.values)


    def compare(s_word, t_word):
        if len(s_word) != len(t_word):
            return False

        s_counter = Counter(s_word)
        t_counter = Counter(t_word)

        return s_counter == t_counter  # Slow!!


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for s in strs:
            # map to a 26 digits counter
            counter = [0] * 26

            for c in s:
                counter[ord(c) - ord('a')] += 1

            res[tuple(counter)].append(s)

        return list(res.values())

