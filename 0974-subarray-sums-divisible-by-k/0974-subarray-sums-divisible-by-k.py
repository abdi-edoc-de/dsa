class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res, prefix, visited = 0, 0 , defaultdict(int)
        visited[0] = 1
        for num in nums:
            prefix = (prefix + num) % k
            res += visited[prefix]
            visited[prefix] += 1
        return res
    