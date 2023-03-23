class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        nums = set()
        for l in range(len(s) - k+1):
            nums.add(s[l:l+k])
        if len(nums) == 2**k:
            return True
        return False 