class Solution:
    def numDistinct(self, s: str, t: str):
        m, n = len(t), len(s)
        dp = [1] + [0] * m
        for i in range(n):
            for j in range(min(i + 1, m), 0, -1):
                if s[i] == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[m]