class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        l = 1
        for r in range(1, len(nums)):
            if nums[l-1] != nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return l
            
        