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
        sorted_list = SortedList()
        for i in range(len(nums)):
            if i > indexDiff:
                sorted_list.remove(nums[i - indexDiff - 1])
            pos = sorted_list.bisect_left(nums[i] - valueDiff)
            if pos != len(sorted_list) and sorted_list[pos] - nums[i] <= valueDiff:
                return True
            sorted_list.add(nums[i])
        return False
# # Example usage
# sol = Solution()
# print(sol.findPair([1, 2, 3, 4], 2, 1))  # Example input
