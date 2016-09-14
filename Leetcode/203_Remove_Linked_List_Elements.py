# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head

        p1 = dummy
        p2 = head
        while p2 is not None:
        	if p2.val != val:
        		p1.next = p2
        		p1 = p2
        	p2 = p2.next
        p1.next = None
        return dummy.next

# Space: O(1)
# Time: O(n)