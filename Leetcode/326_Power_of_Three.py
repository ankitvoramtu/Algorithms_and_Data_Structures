import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        x = math.log(n, 3) // 1 + 1
        return math.pow(3, x) % n == 0
# Time: O(1)
# Space: O(1)
