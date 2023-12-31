# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
from sortedcontainers import SortedList
    
class Solution:
    # def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
    #     n = len(nums)
    #     for i in range(n):
    #         for j in range(i + 1, min(i + 1 + indexDiff, n)):
    #             if abs(nums[i] - nums[j]) <= valueDiff:
    #                 return True
    #     return False

    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        window = SortedList()
        for i in range(len(nums)):
            if i > indexDiff:
                window.remove(nums[i - indexDiff - 1])
            pos = window.bisect_left(nums[i] - valueDiff)
            if pos != len(window) and window[pos] - nums[i] <= valueDiff:
                return True
            window.add(nums[i])
        return False
# # Example usage
# sol = Solution()
# print(sol.findPair([1, 2, 3, 4], 2, 1))  # Example input
