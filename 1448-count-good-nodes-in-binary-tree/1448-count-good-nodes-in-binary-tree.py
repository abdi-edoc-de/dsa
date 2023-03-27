# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_node):
            if not root: return 0
            val = dfs(root.left, max(max_node, root.val)) + dfs(root.right,max(max_node, root.val) ) 
            val += 1 if root.val >= max_node else 0
            return val
        return dfs(root, -(sys.maxsize-1))
            