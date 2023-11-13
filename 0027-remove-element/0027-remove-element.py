class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        right = len(nums)-1
        if right == -1: return 0
       
        
        left = 0
        
        while left < right:
            if nums[right] == val: 
                right -= 1
                continue
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1               
            left += 1
        next = 0
        while next < len(nums) and nums[next] != val:
            next += 1
        return next
        