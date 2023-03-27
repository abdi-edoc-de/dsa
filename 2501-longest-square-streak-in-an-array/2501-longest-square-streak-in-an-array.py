class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dp , nums_set = {}, set(nums)
        def dfs(value):
            if value in dp: return dp[value]
            if value ** 2 in nums_set:
                dp[value] =  1 + dfs(value ** 2)
            else:
                dp[value] = 1
            return dp[value]
        result = 0
        for num in nums:
            result = max(result, dfs(num))
        print(result)
        return -1 if result < 2 else result 