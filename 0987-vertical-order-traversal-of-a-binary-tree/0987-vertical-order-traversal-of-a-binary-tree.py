# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic, result = defaultdict(list), []
        def dfs(root, row, col):
            if root:
                dic[col].append((row, root.val))
                dfs(root.left, row+1, col-1)
                dfs(root.right, row+1, col+1)
        dfs(root, 0 ,0)
        for key in sorted(dic.keys()):
            dic[key].sort()
            arr = []
            for _, val in dic[key]:
                arr.append(val)
            result.append(arr)
        return result
            
    
            