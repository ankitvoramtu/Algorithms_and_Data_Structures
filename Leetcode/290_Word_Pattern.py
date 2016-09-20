class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l = str.split(" ")
        print l
        if len(pattern) != len(l):
        	return False
        d1 = {}
        d2 = {}
        print len(pattern)
        for i in range(0, len(pattern)):
            print i
            if pattern[i] not in d1:
                if l[i] in d2:
                    return False
                else:
                    d1[pattern[i]] = l[i]
                    d2[l[i]] = pattern[i]
            else:
                if l[i] not in d2:
                    return False
                else:
                    if d2[l[i]] != pattern[i]:
                        return False
        return True
