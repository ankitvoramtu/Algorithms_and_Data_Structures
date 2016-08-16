# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    	if root == null:
    		return True
    	return helper(root.left, root.right)
    
    def helper(leftNode, rightNode):
    	if leftNode == null and rightNode == null:
    		return True
    	if leftNode or rightNode == null:
    		return False
    	return leftNode.val == rightNode.val & helper(leftNode.right, rightNode.left) & helper(leftNode.right, rightNode.left)