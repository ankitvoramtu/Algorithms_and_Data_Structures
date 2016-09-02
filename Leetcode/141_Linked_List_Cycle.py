# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
        	return False
        P1 = head
        P2 = P1.next
        while True:
        	if P2 is None or P2.next is None:
        		return False
        	if P1 == P2:
        		return True
        	P1 = P1.next
        	P2 = P2.next.next
