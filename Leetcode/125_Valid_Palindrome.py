class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            while not s[i].isalnum():
                i = i + 1
            while not s[j].isalnum():
                j = j - 1
            if i <= j:
                if s[i].lower() == s[j].lower():
                    i = i + 1
                    j = j - 1
                else:
                    return False
            else:
                return False

        return True

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].salnum():
                l = l + 1
            while l < r and not s[r].salnum():
                r = r + 1
            if s[l].lower() != s[r].lower():
                return False
            l = l + 1
            r = r - 1
        return True
