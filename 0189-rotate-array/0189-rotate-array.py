class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        result = [0] * n
        k = k % n
        
        for i in range(n):
            index = (i+k) % n
            result[index] = nums[i]
        
        for i in range(n):
            nums[i]=result[i]