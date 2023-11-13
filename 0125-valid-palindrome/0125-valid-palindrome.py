class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = []
        
        for c in s:
            if c.isalnum():
                cleaned.append(c.lower())
        n = len(cleaned)
        for i in range(n):
            if cleaned[i] != cleaned[n-i-1]:
                return False
        return True