# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return helper(root) >= 0

    def helper(root):
    	if root is None:
    		return 0

    	left = helper(root.left)
    	right = helper(root.right)
    	if left < 0 or right < 0:
    		return -1
    	if abs(left - right) > 1:
    		return -1
    	return max(left, right) + 1
