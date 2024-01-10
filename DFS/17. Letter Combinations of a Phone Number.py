17. Letter Combinations of a Phone Number

# Backtrack

DAIL_ALPH = {
    2:['a','b','c'],
    3:['d','e','f'],
    4:['g','h','i'],
    5:['j','k','l'],
    6:['m','n','o'],
    7:['p','q','r','s'],
    8:['t','u','v'],
    9:['w','x','y','z']

}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n < 1:
            return []

        cmb = []
        res = []

        def backtrack(index):
            # basecase
            if index == n:
                res.append("".join(cmb))
                return
            else:
                choices = DAIL_ALPH[int(digits[index])]
                for letter in choices:
                    cmb.append(letter)
                    backtrack(index+1)
                    cmb.pop()

        backtrack(0)

        return res


