class Solution:
    def numDistinct(self, s: str, t: str):
        n, m = len(s), len(t)
        dp = [1] + [0] * m
        for i in range(1, n + 1):
            for j in range(min(i, m), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[m]