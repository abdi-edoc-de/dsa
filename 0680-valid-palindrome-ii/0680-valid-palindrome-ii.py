class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPali(left, right, er):
            if left > right:
                return True
            if s[left] == s[right]:
                return isPali(left+1, right-1, er)
            elif er:
                return isPali(left, right-1, not er) or isPali(left+1, right, not er)
            return False
        return isPali(0, len(s)-1 , True)
    