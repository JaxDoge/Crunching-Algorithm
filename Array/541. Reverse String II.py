541. Reverse String II


# Double Pointers

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        if n < 2:
            return s

        sList = list(s)

        fast, slow = 0, 0
        end = -1
        while fast <= n:
            # find the end point of an exchange segment
            if fast - slow == k:
                end = fast - 1

            # if fast is 2 * k indices far away from slow, or fast is out of bound
            # the exchanging program launchs
            if fast - slow == 2*k or fast == n:
                # if the fast is not far enough, the end pointer will smaller than slow pointer
                if end < slow:
                    end = fast - 1
                while slow < end:
                    sList[slow], sList[end] = sList[end], sList[slow]
                    slow += 1
                    end -= 1

                slow = fast

            fast += 1

        return "".join(sList)


# Or just

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        t = list(s)
        for i in range(0, len(t), 2 * k):
            t[i: i + k] = reversed(t[i: i + k])
        return "".join(t)
