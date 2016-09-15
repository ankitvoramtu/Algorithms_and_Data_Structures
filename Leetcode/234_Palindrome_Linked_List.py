# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = []
        p = head
        while p is not None:
        	l.append(p.val)
        	p = p.next
        i = 0
        while i < len(l) / 2:
        	if l[i] != l[-(i+1)]:
        		return False
        	i = i + 1
        return True
