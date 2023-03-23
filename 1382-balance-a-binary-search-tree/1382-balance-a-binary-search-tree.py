# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def dfs(root):
            if not root: return    
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        def dfs1(left, right):
            if left > right: return 
            mid = left + (right - left)//2
            node = TreeNode(arr[mid])
            node.left, node.right = dfs1(left, mid-1), dfs1(mid+1, right)
            return node
        return dfs1(0, len(arr)-1) 