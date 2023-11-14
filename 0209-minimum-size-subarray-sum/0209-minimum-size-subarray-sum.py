class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, check, summ, best = 0 , False, 0, len(nums)
        
        for r in range(len(nums)):
            summ += nums[r]
            
            if summ >= target:
                check = True
                while summ - nums[l] >= target and l < r:
                    summ -= nums[l]
                    l += 1
                best = min(best, (r-l+1))
        if check:
            return best
        return 0
            