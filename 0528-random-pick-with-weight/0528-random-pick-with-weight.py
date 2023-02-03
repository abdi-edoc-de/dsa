class Solution:

    def __init__(self, w: List[int]):
        self.prefix = w
        for i in range(1,len(w)):
            self.prefix[i] += self.prefix[i-1]
        
    def pickIndex(self) -> int:
        rand = random.randint(1,self.prefix[-1])
        return self.helper(rand)
    def helper(self, target) :
        l, r = 0, len(self.prefix)-1
        while l<r:
            mid = (l+r)//2
            if target <= self.prefix[mid]:
                r = mid
            else:
                l = mid+1
        return l
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()