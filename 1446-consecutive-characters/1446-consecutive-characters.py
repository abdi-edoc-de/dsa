class Solution:
    def maxPower(self, s: str) -> int:
        count , power, l= {}, 1, 0
        count[s[0]] = 1
        for r in range(1, len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            if len(count) == 1:
                power = max(count[s[r]], power)
            else:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
                
            power = max(power, r-l)
        return power
                