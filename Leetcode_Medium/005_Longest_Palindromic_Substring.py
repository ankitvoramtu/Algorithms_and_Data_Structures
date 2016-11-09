'''

005_Longest_Palindromic_Substring

Given a string S, find the longest palindromic substring in S. You may assume 
that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
        	return s
        start = 0
        end = 0
        for i in range(0, len(s)):
        	len1 = expand_around_center(self,s, i, i)
        	len2 = expand_around_center(self,s, i ,i + 1)
        	len_cur = max(len1, len2)
        	if len_cur > end - start:
        		start = i - (len_cur - 1) / 2
        		end = i + len_cur / 2
        return s[start: (end+1)]

    def expand_around_center(self, s, l, r):
    	while l >= 0 and r <= len(s) and s[l] == s[r]:
    		l = l - 1
    		r = r + 1
    	return l - r + 1