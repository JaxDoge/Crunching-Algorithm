394. Decode String



# Stack
class Solution(object):
    def __init__(self):
        pass

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        readStack = []
        p = 0
        n = len(s)

        while p < n:
            # read digit number
            preNum = 0
            while s[p].isdecimal():
                preNum = preNum * 10 + int(s[p])
                p += 1

            if preNum:
                readStack.append(preNum)

            if s[p] != "]":
                readStack.append(s[p])
            else:
                # Start decode
                wordL = []
                while readStack[-1] != "[":
                    wordL.append(readStack.pop())
                readStack.pop()  # pop [
                wordL.reverse()
                word = "".join(wordL)
                word = word * readStack.pop()
                readStack.append(word)
            p += 1


        return "".join(readStack)

