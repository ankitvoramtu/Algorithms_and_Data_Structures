class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for i in range(1, len(s) + 1):
            dig = ord(s[-i]) - ord("A") + 1
            cur = dig * 26 ** i
            ret = ret + cur
        return ret
