class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major , count= nums[0] , 0
        
        for i in range(len(nums)):
            if count == 0:
                major , count = nums[i], count + 1
            elif major == nums[i]:
                count += 1
            else:
                count -=1
        return major