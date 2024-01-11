class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
    # def canMakePaliQueries(s, queries):
        prefix = [[0]*26]
        for i in range(len(s)):
            cnt = prefix[-1][:]
            cnt[ord(s[i])-ord('a')] += 1
            prefix.append(cnt)

        res = []
        for l, r, k in queries:
            cnt = [prefix[r+1][i] - (prefix[l][i] if l > 0 else 0) for i in range(26)]
            res.append(sum(v%2 for v in cnt) // 2 <= k)
        return res