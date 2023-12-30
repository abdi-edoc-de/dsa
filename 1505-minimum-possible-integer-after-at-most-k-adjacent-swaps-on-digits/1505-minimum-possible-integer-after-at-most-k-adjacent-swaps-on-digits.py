class BIT:
    def __init__(self, n):
        self.n = n
        self.nodes = [0] * (n + 1)

    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.nodes[i] += delta
            i += i & -i

    def query(self, i):
        total = 0
        while i > 0:
            total += self.nodes[i]
            i -= i & -i
        return total

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        qs = [[] for _ in range(10)]
        n = len(num)
        
        for i in range(n):
            qs[int(num[i])].append(i)
        
        lhs = ""
        removed = [False] * n
        tree = BIT(n)
        
        while k > 0:
            found = False
            for d in range(10):
                if qs[d]:
                    pos = qs[d][0]
                    shifted = tree.query(pos)
                    if pos - shifted <= k:
                        k -= pos - shifted
                        tree.update(pos, 1)
                        qs[d].pop(0)
                        lhs += str(d)
                        removed[pos] = True
                        found = True
                        break
            if not found:
                break
        
        rhs = ""
        for i in range(n):
            if not removed[i]:
                rhs += num[i]
        
        return lhs + rhs
