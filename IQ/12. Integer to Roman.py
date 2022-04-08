12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        import collections
        roman_table = {
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC'
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'
        }

        roman_table = collections.OrderedDict(reversed(list(roman_table.items())))

        ans = list()
        for key, value in roman_table.items():
            while num >= key:
                num -= key
                ans.append(value)

        return ''.join(ans)
