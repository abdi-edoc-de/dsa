class Solution:
    def __init__(self):
        self.d = []
    
    def minNumberOfSemesters(self, n, relations, k):
        i = [0] * n
        a = [[] for _ in range(n)]

        for r in relations:
            i[r[1] - 1] += 1
            a[r[0] - 1].append(r[1] - 1)

        m = (1 << n) - 1
        self.d = [-1] * (m + 1)

        return self.s(m, i, a, k)
    
    def s(self, m, i, a, k):
        if m == 0:
            return 0
        if self.d[m] != -1:
            return self.d[m]

        r = float('inf')
        n = [j for j in range(len(i)) if m & (1 << j) and i[j] == 0]
        v = len(n)
        c = self.u(n, min(v, k))

        for j in c:
            nm = m
            ni = i.copy()

            for x in j:
                nm ^= (1 << x)
                for y in a[x]:
                    ni[y] -= 1
            
            r = min(r, 1 + self.s(nm, ni, a, k))

        self.d[m] = r
        return r

    def g(self, n, k, s, c, r):
        if k == 0:
            r.append(c[:])
            return

        for j in range(s, len(n)):
            c.append(n[j])
            self.g(n, k - 1, j + 1, c, r)
            c.pop()

    def u(self, n, k):
        r = []
        c = []
        self.g(n, k, 0, c, r)
        return r
