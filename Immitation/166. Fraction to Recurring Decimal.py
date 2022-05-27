166. Fraction to Recurring Decimal



#  simulate division
#  we could use division operation
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        # Sign flag
        negFlag = False
        if numerator < 0 and denominator > 0:
            negFlag = True
            numerator = -numerator
        elif numerator > 0 and denominator < 0:
            negFlag = True
            denominator = -denominator
        else:
            numerator = abs(numerator)
            denominator = abs(denominator)


        n = len(str(numerator))
        nuList =[int(x) for x in str(numerator)]
        from collections import defaultdict, deque
        res = deque()
        memo = defaultdict(int)
        loopStart = -1

        def get(idx):
            nonlocal nuList
            if idx >= n:
                return 0
            return nuList[idx]

        def subDivision(de, remainder, Idx):
            nonlocal denominator, n, res, memo, loopStart
            subNu = remainder * 10 + get(Idx)
            if Idx >= n:
                if remainder == 0:
                    return
                elif subNu in memo and memo[subNu] >= n:
                    loopStart = memo[subNu]
                    return
            
                memo[subNu] = Idx
            
            re = subNu % de             
            res.append(subNu // de)
            subDivision(de, re, Idx + 1)

        subDivision(denominator, 0, 0)
        while res[0] == 0 and n > 1:
            res.popleft()
            n -= 1
            loopStart -= 1
            if n == 1:
                break

        res = [str(x) for x in res]

        if negFlag:
            ans = "-" + "".join(res[0:n])
        else:
            ans = "".join(res[0:n])
        
        if len(res) > n:
            ans = ans + "."
            if loopStart > 0:
                ans = ans + "".join(res[n:loopStart]) + "(" + "".join(res[loopStart:]) + ")"
            else:
                ans = ans + "".join(res[n:])

        return ans



