class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, count = 1, 1
        
        for r in range(1, len(nums)):
            if nums[l-1] == nums[r] and count == 1:
                nums[l] = nums[r]
                l += 1
                count = 2
            elif nums[l-1] != nums[r]:
                count = 1
                nums[l] = nums[r]
                l+=1
        return l