class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        dp = {}
        def dfs(cur, prev, pOp):
            nonlocal dp
            if (cur, prev) in dp:
                return dp[(cur,prev)]
            if cur == n:
                return 0
            if cur > n or cur + prev > n:
                return sys.maxsize
            if pOp:
                dp[(cur, prev)] = 1 + dfs(cur+prev, prev, not pOp)
            else:
                dp[(cur, prev)] = 1 + min(dfs(cur, cur, not pOp), dfs(cur+prev, prev, pOp))
            return dp[(cur, prev)]
        return 1 + dfs(1,1,True)
            