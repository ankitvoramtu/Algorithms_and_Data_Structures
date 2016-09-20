# Solution 1: Dictionary
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d = {}
        # Add elements to d
        for i in range(0, len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] = d[s[i]] + 1
        # Remove elements to d
        for i in range(0, len(t)):
            if t[i] not in d:
                return False
            else:
                d[t[i]] = d[t[i]] - 1
        # Check if values for all keys are 0
        for e in d:
            if d[e] != 0:
                return False
        return True

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        l1 = []
        l2 = []
        for i in range(0, len(s)):
            l1.append(s[i])
            l2.append(t[i])
        l1.sort() 
        l2.sort()
        return l1 == l2