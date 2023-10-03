class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count , result = defaultdict(int) , 0
        
        for num in nums:
            result += count[num]
            count[num] += 1
        return result 
        