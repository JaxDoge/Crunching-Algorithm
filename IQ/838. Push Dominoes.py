838. Push Dominoes


# simulation
# the final state of a serial upright dominoes is determined by the left end and right end
# if there is no left end falling domino, we could assume there is one which is falling to the left
# same as the right end
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dList = list(dominoes)
        n = len(dList)
        i = 0 
        left = 'L'

        while i < n:
            # firstly we try to find the end of a consecutive dots
            # note that there may be no dot at all
            j = i
            # as long as j is valid, move j forward
            while j < n and dList[j] == '.':
                j += 1

            # in any case, j point to the right end, so 
            right = dList[j] if j < n else 'R'

            # Case one, the direction of left and right is the same
            # change every element in [i,j)
            if left == right:
                while i < j:
                    dList[i] = left
                    i += 1

            # Case two, they move to each other, change every element in [i, j-1] from both sides
            elif left == 'R' and right == 'L':
                k = j - 1
                # the domino in the middle should be upright, which means untouched
                while i < k:
                    dList[i] = 'R'
                    dList[k] = 'L'
                    i += 1
                    k -= 1

            # Case three, they move oppsite directions
            # do nothing

            # the right end become the new left end
            left = right
            # j + 1 become the start of the next
            i = j + 1

        return ''.join(dList)