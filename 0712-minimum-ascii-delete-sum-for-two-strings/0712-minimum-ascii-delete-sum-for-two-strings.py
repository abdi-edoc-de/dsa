class Solution(object):
    def minimumDeleteSum(self, str1, str2):
        k = len(str1)
        m = len(str2)
        dp = [[0 for x in range(m + 1)] for x in range(k + 1)]

        for i in range(1, k + 1):
            dp[i][0] = dp[i - 1][0] + ord(str1[i - 1])

        for i in range(1, m + 1):
            dp[0][i] = dp[0][i - 1] + ord(str2[i - 1])

        for i in range(1, k + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(str1[i - 1]), dp[i][j - 1] + ord(str2[j - 1]))

        return dp[k][m]