class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = deque()
        queue.append(root)
        queue.append(root)

        while queue:
            r1 = queue.popleft()
            r2 = queue.popleft()

            if not r1 and not r2:
                continue

            if not r1 or not r2:
                return False

            if r1.val != r2.val:
                return False

            queue.append(r1.left)
            queue.append(r2.right)
            queue.append(r1.right)
            queue.append(r2.left)

        return True