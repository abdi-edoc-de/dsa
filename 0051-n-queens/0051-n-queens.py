class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        a = []
        b = [['.' for _ in range(n)] for _ in range(n)]
        for c in range(n):
            for d in range(n):
                b[c][d] = 'Q'
                self.d(a, [(c, d)], c, d, n, b)
                b[c][d] = '.'

        return a
    
    def d(self, a, e, c, d, n, b):
        if len(e) == n:
            f = []
            for g in b:
                f.append(''.join(g))
            a.append(f)
            return 
        for h in range(c + 1, n):
            for i in range(n):
                j = False
                if (i, h) == (c, d): continue
                for k, l in e:
                    if h == k or i == l or (h - k)/(i - l) == 1 or (h - k)/(i - l) == -1:
                        j = True; break
                if j: continue
                b[h][i] = 'Q'
                e.append((h, i))
                self.d(a, e, h, i, n, b)
                b[h][i] = '.'
                e.pop()
