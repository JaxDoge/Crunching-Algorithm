1044. Longest Duplicate Substring


# Approach #1, dichotomy + string hash
# Rabin-Karp + dichotomy
# Last 2 unit tests TLE!!
class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)   # the longest dupsubstr has length n - 1
        l = 1
        r = n
        if n < 2:
            return ""

        def check(subLen):
            # nonlocal n, s
            memo = set()
            strHash = 0
            base = 1
            prime = 31

            for i in range(subLen):
                strHash = strHash * prime + (ord(s[i]) - ord("a") + 1)
                base *= prime

            memo.add(strHash)
            # Slide window
            # kick out the head character and move in the tail one
            for i in range(subLen, n):
                strHash = strHash * prime - (ord(s[i - subLen]) - ord("a") + 1) * base + (ord(s[i]) - ord("a") + 1)
                if strHash in memo:
                    return i - subLen + 1
                memo.add(strHash)

            return -1 

        pos = -1
        subLen = 0
        while l < r:
            mid = l + (r - l) // 2
            start = check(mid)
            if start != -1:
                subLen = mid
                pos = start
                l = mid + 1
            else:
                r = mid 

        if pos == -1:
            return ""
        return s[pos:pos + subLen]


# Double hash
class Solution(object):
    def longestDupSubstring(self, s):
        n = len(s)   # the longest dupsubstr has length n - 1
        l = 1
        r = n
        if n < 2:
            return ""

        # encode s
        arr = [ord(x) - ord("a") + 1 for x in s]
        from random import randint
        prime1 = randint(26, 100)
        prime2 = randint(26, 100)
        mod1, mod2 = randint(10**5, 2**31-1), randint(10**5, 2**31-1)

        def check(subLen):
            # nonlocal n, s
            memo = set()
            hash1 = 0
            hash2 = 0
            base1, base2 = pow(prime1, subLen, mod1), pow(prime2, subLen, mod2)

            for i in range(subLen):
                hash1 = (hash1 * prime1 + arr[i]) % mod1
                hash2 = (hash2 * prime2 + arr[i]) % mod2


            memo.add((hash1, hash2))
            # Slide window
            # kick out the head character and move in the tail one
            for i in range(subLen, n):
                hash1 = (hash1 * prime1 - arr[i - subLen] * base1 + arr[i]) % mod1
                hash2 = (hash2 * prime2 - arr[i - subLen] * base2 + arr[i]) % mod2
                if (hash1, hash2) in memo:
                    return i - subLen + 1
                memo.add((hash1, hash2))

            return -1 

        pos = -1
        subLen = 0
        while l < r:
            mid = l + (r - l) // 2
            start = check(mid)
            if start != -1:
                subLen = mid
                pos = start
                l = mid + 1
            else:
                r = mid 

        if pos == -1:
            return ""
        return s[pos:pos + subLen]



# suffix array + radix sort
class suffix:
     
    def __init__(self):
         
        self.index = 0
        self.rank = [0, 0]

class Solution(object):
    def longestDupSubstring(self, s):

        # imporve sort to radix sort
        # Note that the rank have to start from 0 not -1
        def countingSort(array, maxN, rk):
            size = len(array)
            res = [suffix()] * size
            count = [0] * (maxN + 1)

            for num in array:
                count[num.rank[rk]] += 1

            for i in range(1, maxN+1):
                count[i] += count[i - 1]

            for i in range(size - 1, -1, -1):
                curN = array[i]
                cum = count[curN.rank[rk]]
                res[cum - 1] = curN
                count[curN.rank[rk]] -= 1

            for i in range(size):
                array[i] = res[i]

            return



        def radixSort(array):
            # sort rank1 then sort rank0
            maxRank = max(26, len(array))
            countingSort(array, maxRank, 1)
            countingSort(array, maxRank, 0)
            return


        def buildSuffixArray(txt):
            n = len(txt)

            suffixes = [suffix() for _ in range(n)]
         
            # Initialize suffixes array
            for i in range(n):
                suffixes[i].index = i
                suffixes[i].rank[0] = (ord(txt[i]) -
                                       ord("a") + 1)
                suffixes[i].rank[1] = (ord(txt[i + 1]) -
                                ord("a") + 1) if ((i + 1) < n) else 0

            radixSort(suffixes)
            idxToPos = [0] * n

            # first 2 characters is sorted, then it is first 4 need be sorted, then 8 and so on
            k = 2  # k is the sorted length, which cannot exceed n
            while k < n:
                # re-assign rank 0, and store position in idxToPos to re-assign rank1
                rank = 1
                previousRk = suffixes[0].rank[0]
                suffixes[0].rank[0] = rank
                idxToPos[suffixes[0].index] = 0

                for i in range(1, n):
                    # same rank as before
                    if (suffixes[i].rank[0], suffixes[i].rank[1]) == (previousRk, suffixes[i - 1].rank[1]):
                        previousRk = suffixes[i].rank[0]
                        suffixes[i].rank[0] = rank
                    else:
                        rank += 1
                        previousRk = suffixes[i].rank[0]
                        suffixes[i].rank[0] = rank

                    idxToPos[suffixes[i].index] = i
                
                # re-assign rank1
                for i in range(n):
                    nextIdx = suffixes[i].index + k
                    suffixes[i].rank[1] = suffixes[idxToPos[nextIdx]].rank[0] if nextIdx < n else 0

                radixSort(suffixes)
                k *= 2

            sa = [sf.index for sf in suffixes]

            return sa

        sa = buildSuffixArray(s)

        length = len(s)
        # find LCP
        # in O(n) time complexity
        k = 0
        # build the rk array
        rk = [0] * length
        # build the rk-LCP array
        LCP = [0] * length

        for i in range(length):
            rk[sa[i]] = i

        for i in range(length):
            if rk[i] == 0:
                continue
            j = sa[rk[i] - 1]
            k = k - 1 if k > 0 else 0
            while i + k < length and j + k < length and s[i + k] == s[j + k]:
                k += 1
            LCP[rk[i]] = k

        start = -1
        subLen = 0
        for i in range(1, length):
            if LCP[i] > subLen:
                subLen = LCP[i]
                start = sa[i]

        return "" if subLen == 0 else s[start:start + subLen]