class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # Add 1 to the last digit, result might be 10
        digits[-1] += 1

        i = len(digits) - 1
        while i >= 1 and digits[i] == 10:
            digits[i] = 0
            digits[i - 1] += 1
            i = i - 1

        # Check first digit
        if digits[0] == 10:
            digits[0] = 0
            digits = [1] + digits

        return digits
