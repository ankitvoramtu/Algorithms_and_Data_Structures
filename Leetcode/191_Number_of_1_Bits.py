class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        for i in range(32):
			if n & 1:
				ret = ret + 1
        	n >>= 1
        return ret