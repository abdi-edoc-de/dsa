class Solution:
    def findDuplicates(self, nums):
        num_set = set()
        duplicates = set()
        for num in nums:
            if num in num_set:
                duplicates.add(num)
            else:
                num_set.add(num)
        return list(duplicates)

    
