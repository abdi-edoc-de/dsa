class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index, result, l = {}, 0, 0
        for r in range(len(s)):
            if s[r] in index:
                ind = index[s[r]]
                for i in range(l, index[s[r]]):
                    del index[s[i]]
                l = ind + 1
            index[s[r]], result = r, max(result, r-l+1)
        return result
            
                