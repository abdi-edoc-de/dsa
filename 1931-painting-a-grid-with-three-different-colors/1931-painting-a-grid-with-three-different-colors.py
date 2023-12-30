class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    def generate_mask(self, m, msk, masks, pre_msk, pre_col):
        if m == 0:
            masks.append(msk)
            return
        for i in range(1, 4):
            if pre_col != i and ((pre_msk >> ((m - 1) * 2)) & 3) != i:
                self.generate_mask(m - 1, msk | (i << (m - 1) * 2), masks, pre_msk, i)

    def func(self, m, n, idx, msk, dp, msk_map):
        if idx == n:
            return 1
        if dp[idx][msk] != -1:
            return dp[idx][msk]
        if msk not in msk_map:
            msk_map[msk] = []
            self.generate_mask(m, 0, msk_map[msk], msk, 0)
        ans = 0
        for cur_msk in msk_map[msk]:
            ans += self.func(m, n, idx + 1, cur_msk, dp, msk_map)
            ans %= self.mod
        dp[idx][msk] = ans
        return ans

    def colorTheGrid(self, m, n):
        dp = [[-1 for _ in range(1 << (2 * m))] for _ in range(n)]
        msk_map = {}
        return self.func(m, n, 0, 0, dp, msk_map)
# Example usage
sol = Solution()
result = sol.colorTheGrid(3, 3)  # Example arguments
print(result)
