class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ops , dic = 0, {}
        for num in nums:
            if k - num in dic:
                ops += 1
                dic[k-num] -= 1
                if dic[k-num] == 0:
                    del dic[k-num]
            else:
                if num not in dic:
                    dic[num] = 1
                else:
                    dic[num] += 1
        return ops
    