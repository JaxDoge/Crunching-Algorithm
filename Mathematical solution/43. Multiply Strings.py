#  mimic pre-algebra multiplication, multiply by digits
#  double pointers
#  num1[i] * num2[j] return the part result in res[i+j] and res[i+j+1]
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Bad case
        if num1 == '0' or num2 == '0':
            return '0'
        m = len(num1)
        n = len(num2)
        # the final outcome won't have more than m + n digits
        res = [0] * (m + n)
        # start from the right most index
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                sub_res = int(num1[i]) * int(num2[j])
                #  find the corresponding res indices
                p1 = i + j
                p2 = p1 + 1
                sub_sum = sub_res + res[p2]
                # get carrier
                res[p2] = sub_sum % 10
                res[p1] = res[p1] + sub_sum // 10

        # find the left most non-zero index
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1

        return ''.join([str(x) for x in res[i:]])



# Not sure if it is the best way
# DFS
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":  
            return "0"

        n = len(num1)
        m = len(num2)
        from collections import deque

        def singleProduct(p2, ansP):
            nonlocal num1, num2, n, m

            if p2 >= m:
                return ansP

            curMul = int(num2[p2])
            p1 = n - 1
            carry = 0
            curProd = deque()
            while p1 >= 0:
                product = int(num1[p1]) * curMul + carry
                if product > 9:
                    carry = product // 10
                else:
                    carry = 0
                curProd.appendleft(product % 10)
                p1 -= 1
            
            if carry != 0:
                curProd.appendleft(carry)
            
            if not ansP:
                return singleProduct(p2 + 1, curProd)
            
            ansP.append(0)
            tmp = deque()
            i = len(ansP) - 1
            j = len(curProd) - 1
            
            carry = 0
            while i >= 0 and j >= 0:
                sumup = ansP[i] + curProd[j] + carry
                if sumup > 9:
                    carry = 1
                else:
                    carry = 0
                tmp.appendleft(sumup % 10)
                i -= 1
                j -= 1
            
            while i >= 0:
                sumup = ansP[i] + carry
                if sumup > 9:
                    carry = 1
                else:
                    carry = 0
                tmp.appendleft(sumup % 10)     
                i -= 1   

            while j >= 0:
                sumup = curProd[j] + carry
                if sumup > 9:
                    carry = 1
                else:
                    carry = 0
                tmp.appendleft(sumup % 10)     
                j -= 1

            if carry != 0:
                tmp.appendleft(carry)    
            
            if p2 == m - 1:
                return tmp
            
            return singleProduct(p2 + 1, tmp)

        ans = singleProduct(0, deque())
        return "".join([str(x) for x in ans])

