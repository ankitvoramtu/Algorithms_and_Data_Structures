class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # Rephrase: if needle is substring of haystack
        # if len(needle) > len(haystack):
        # return -1

        # Normal case
        for i in range(0, len(haystack) - len(needle) + 1):
            j = 0
            while j < len(needle):
                if needle[j] == haystack[i + j]:
                    j = j + 1
                else:
                    break
            if j == len(needle):
                return i
        return -1
