class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def dfs(flag):
            l, r = 0, len(nums) - 1
            best = -1
            while l <= r:
                mid = l + (r - l)//2
                if target == nums[mid]:
                    best = mid
                    if flag:
                        l = mid + 1
                    else:
                        r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return best
        return [dfs(False), dfs(True)]
        
            