class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, best = 0, len(nums)-1, nums[(len(nums)-1)//2]
        
        while l <= r:
            mid = l + (r-l)//2
            best = min(best, nums[mid])
            if nums[l] == nums[mid]:
                l += 1
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return best
    