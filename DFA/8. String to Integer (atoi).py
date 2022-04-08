8. String to Integer (atoi)


# Deterministic Finite Automaton

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Automaton:
    def __init__(self):
        # initial state
        self.state = 'start'
        # sign
        self.sign = 1
        # result
        self.ans = 0
        # transition function
        self.table = {
            'start':['start', 'signed', 'in_number', 'end'],
            'signed':['end','end','in_number','end'],
            'in_number':['end','end','in_number','end'],
            'end':['end','end','end','end']
        }

    def get_col(self, c):
        # map any character to certain acceptable input
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        # change state based on c
        self.state = self.table[self.state][self.get_col(c)]
        # check integer overflow, update ans
        if self.state == 'in_number':
            tmp = (INT_MAX - int(c)) / 10 if self.sign == 1 else (-INT_MIN - int(c)) / 10
            if self.ans >= tmp:
                self.ans = INT_MAX if self.sign == 1 else -INT_MIN
            else:
                self.ans = self.ans * 10 + int(c)
        if self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans
