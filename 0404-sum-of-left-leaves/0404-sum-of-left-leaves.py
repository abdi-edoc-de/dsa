# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        def traverse(node, isLeft):
            if not node: return 0
            if isLeft and not node.left and not node.right:
                return node.val
            return traverse(node.left, True) + traverse(node.right, False)
        return traverse(root, False)
        
            