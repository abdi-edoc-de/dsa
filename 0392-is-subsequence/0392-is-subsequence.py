class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        l = 0
        for r in range(len(t)):
            if len(s) == l: return True
            if t[r] == s[l]:
                l+=1
        if len(s) == l: return True
        return False 