65. Valid Number


# complicated DFA
class Solution:
    def __init__(self):
        self.state = 'start'
        self.flag = True
        # E/e, +/-, digits, period
        self.table = {
            'start':['invalid', 'sign', 'integer', 'period'],
            'sign':['invalid', 'invalid', 'integer', 'period'],
            'integer':['sn', 'invalid', 'integer', 'decimal'],
            'period':['invalid', 'invalid', 'decimal', 'invalid'],
            'decimal':['sn', 'invalid', 'decimal', 'invalid'],
            'sn':['invalid', 'sn_sign', 'sn_int', 'invalid'],
            'sn_sign':['invalid', 'invalid', 'sn_int', 'invalid'],
            'sn_int':['invalid', 'invalid', 'sn_int', 'invalid']
        }

    def map(self, c):
        if c in {'E', 'e'}:
            return 0
        elif c in {'+', '-'}:
            return 1
        elif c.isdigit():
            return 2
        elif c == '.':
            return 3
        print('c({0}) is out-bounded'.format(c))
        return 999

    def flow(self, c):
        if c.isalpha() and c not in {'E', 'e'}:
            self.flag = False
            return
        self.state = self.table[self.state][self.map(c)]
        if self.state == 'invalid':
            self.flag = False
        return


    def isNumber(self, s: str) -> bool:
        if len(s) == 0:
            return False


        for c in s:
            self.flow(c)
            if not self.flag:
                return False

        if self.state in {'sign', 'sn', 'sn_sign', 'period'}:
            return False


        return True
