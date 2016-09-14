# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        tmp = head

        ret = None

        while tmp is not None:
            p1 = tmp.next
            tmp.next = ret
            ret = tmp
            tmp = p1
        return ret
