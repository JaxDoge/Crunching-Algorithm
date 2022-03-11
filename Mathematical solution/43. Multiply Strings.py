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



