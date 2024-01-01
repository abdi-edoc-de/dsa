class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBSTHelper(self, root, minVal, maxVal):
        if root is None:
            return True
        if root.val <= minVal or root.val >= maxVal:
            return False
        return (self.isBSTHelper(root.left, minVal, root.val) and 
                self.isBSTHelper(root.right, root.val, maxVal))

    def insertInMap(self, trees, mp, par):
        for t in trees:
            par[t] = t
            if t.left:
                if t.left.val not in mp:
                    mp[t.left.val] = t
                else:
                    return False
            if t.right:
                if t.right.val not in mp:
                    mp[t.right.val] = t
                else:
                    return False
        return True

    def mergeTrees(self, trees, mp, par):
        for t in trees:
            if t.val in mp:
                root = mp[t.val]
                if not self.mergeNode(t, root, mp, par):
                    return False
        return True

    def mergeNode(self, t, root, mp, par):
        if root.right and root.right.val == t.val:
            return self.attachRight(t, root, mp, par)
        elif root.left and root.left.val == t.val:
            return self.attachLeft(t, root, mp, par)
        return True

    def attachRight(self, t, root, mp, par):
        check = float('inf')
        if t.left:
            check = t.left.val
        if check > root.val:
            root.right = t
            par[t] = par[root]
            del mp[t.val]
            return True
        else:
            return False

    def attachLeft(self, t, root, mp, par):
        check = float('-inf')
        if t.right:
            check = t.right.val
        if check < root.val:
            root.left = t
            par[t] = par[root]
            del mp[t.val]
            return True
        else:
            return False

    def canMerge(self, trees):
        mp = {}
        par = {}
        if not self.insertInMap(trees, mp, par):
            return None
        if not self.mergeTrees(trees, mp, par):
            return None
        ans = [t for t, parent in par.items() if t == parent]
        if len(ans) == 1 and self.isBSTHelper(ans[0], float('-inf'), float('inf')):
            return ans[0]
        return None
