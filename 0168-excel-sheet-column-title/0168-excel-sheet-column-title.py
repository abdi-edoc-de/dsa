class Solution:
    def convertToTitle(self, n: int) -> str:  
        if n <= 0:
            return ''
        ans = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ret = ''
        base = 0    
        while n > 0:
            tmp = int(n / (26 ** base))  
            val = tmp % 26
            if val == 0:
                char = 'Z'
                n = n - 26*(26**base)
            else:
                char = ans[val-1]
                n = n - val*(26**base)
            ret = char + ret
            base += 1
        return ret