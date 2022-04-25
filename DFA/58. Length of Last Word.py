58. Length of Last Word


# DFA
class Automation():
    def __init__(self):
        self.word_len = 0
        self.state = 'start'
        self.table = {
        'start':['start', 'inword'],
        'inword':['start', 'inword']
        }

    def map(self, c):
        if c == ' ':
            return 0
        else:
            return 1

    def input(self, c):
        previous = self.state
        self.state = self.table[self.state][self.map(c)]
        # reset counter
        if previous == 'start' and self.state == 'inword':
            self.word_len = 0

        if self.state == 'inword':
            self.word_len += 1


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        auto = Automation()
        for c in s:
            auto.input(c)

        return auto.word_len
