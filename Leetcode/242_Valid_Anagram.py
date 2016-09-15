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