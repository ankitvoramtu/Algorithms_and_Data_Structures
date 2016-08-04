class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Special
        if n == 1:
            return 1
        if n == 2:
            return 2

        # n > 2
        ret = [0] * n
        ret[0] = 1
        ret[1] = 2
        for i in range(2, n):
            ret[i] = ret[i - 2] + ret[i - 1]
        return ret[n - 1]
