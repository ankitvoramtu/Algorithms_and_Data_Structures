'''
017_Letter_Combination_of_a_Phone_Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)
        d = {'2': 'abc', '3': 'edf', '4': 'ghi', '5':'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ret = [''] # initialize ret list
        while i < len(digits): # for each digit, add its correspondance letter to elements in ret
        	for e in ret: # for each element in ret
        		cur = []
        		for j in range(0, len(d[digits[i]])):
        			cur.append(e + d[digits[i]][j])
        	ret = cur
        return ret
［234］
 a, b, c, ad,ae,af,