151. Reverse Words in a String



# DFA + Stack
class Solution:
    def __init__(self):
        self.state = "start"
        self.table = {
                    "start":["space", "in-word"],
                    "space":["space", "in-word"],
                    "in-word":["space", "in-word"]
                    }
        self.res = []


    def code(self, c):
        if c.isspace():
            return 1
        elif c.isspace():
            return 0

    def reverseWords(self, s: str) -> str:
        n = len(s)
        wordS = 0
        wordE = 0
        for i in range(n):
            preState = self.state
            c = s[i]
            self.state = self.table[self.state][self.code(c)]
            if preState != "in-word" and self.state == "in-word":
                wordS = i
            if preState == "in-word" and self.state != "in-word":
                wordE = i
                self.res.append(s[wordS:wordE])
        if self.state == "in-word":
            self.res.append(s[wordS:n])

        self.res.reverse()
        return " ".join(self.res)