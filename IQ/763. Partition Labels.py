763. Partition Labels



#  Intuitive approach
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        from collections import defaultdict, Counter
        letter2F = Counter(s)

        n = len(s)
        if n == 1:
            return [1]

        freq2L = defaultdict(set)
        # initialize the pointer
        fast = 1
        slow = 0
        freq2L[letter2F[s[slow]]].add(s[slow])
        memo = {s[slow]}

        res = []

        while fast < n:
            # the condition of split 
            if len(freq2L[1]) != 0 and len(freq2L) == 1:
                res.append(fast - slow)
                slow = fast
                freq2L.clear()
                memo = {s[slow]}
                freq2L[letter2F[s[slow]]].add(s[slow])
                fast += 1
                continue

            # if we scan this letter before
            if s[fast] in memo:
                freq2L[letter2F[s[fast]]].remove(s[fast])
                # if this frequence bucket is empty, remove it
                if not freq2L[letter2F[s[fast]]]:
                    del freq2L[letter2F[s[fast]]]
                letter2F[s[fast]] -= 1
                freq2L[letter2F[s[fast]]].add(s[fast])
            # if this is a new letter
            else:
                memo.add(s[fast])
                freq2L[letter2F[s[fast]]].add(s[fast])

            fast += 1

        # the last split
        res.append(fast - slow)
        return res



# Better approach, update the furthest end of current subarray

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # scan the array and record the last position of each letter
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord("a")] = i
        
        partition = list()
        start = end = 0
        for i, ch in enumerate(s):
            # update end base on current character, end maybe larger or not
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1
        
        return partition



