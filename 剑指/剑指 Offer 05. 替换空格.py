剑指 Offer 05. 替换空格



class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        sL = s.split(" ")
        return "%20".join(sL)