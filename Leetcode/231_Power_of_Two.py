class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        while n / 2 ** i  > 0:
        	if n % (2 ** i) == 0:
        		return True
        	else:
        		i = i + 1
        return False