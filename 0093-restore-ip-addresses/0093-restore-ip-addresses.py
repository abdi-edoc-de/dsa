class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.possibilities(s, 0, 3)
    
    def possibilities(self, s, start, dots):
        if dots == 0:
            num = int(s[start:])
            if num > 255 or (s[start] == "0" and len(s[start:]) != 1):
                return []
            return [s[start:]]
        res = []
        for i in range(start + 1, len(s)):
            num = int(s[start:i])
            if num > 255 or (s[start] == "0" and len(s[start:i]) != 1):
                break
            res.extend(s[start:i] + '.' + child for child in self.possibilities(s, i, dots - 1))
        return res