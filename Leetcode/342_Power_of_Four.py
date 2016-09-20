# Solution 1: Basic
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """ 
        if num <= 0:
            return False
        while num % 4 == 0:
            num = num / 4
        return num == 1
# Time: O(1)
# Space: O(1)
import math
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """ 
        if n <= 0:
            return False
        x = math.log(n, 4) // 1 + 1
        return math.pow(4, x) % n == 0
# Time: O(1)
# Space: O(1)
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """ 
        if num <= 0:
            return False
        if num & (num - 1) != 0:
            return False
        return num % 3 == 1
# Time: O(1)
# Space: O(1)