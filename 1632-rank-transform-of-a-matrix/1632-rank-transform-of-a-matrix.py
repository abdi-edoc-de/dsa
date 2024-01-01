class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find_u_par(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_u_par(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u, v):
        ulp_u = self.find_u_par(u)
        ulp_v = self.find_u_par(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def matrixRankTransform(self, matrix):
        n, m = len(matrix), len(matrix[0])
        rank = [0] * (m + n)
        d = collections.defaultdict(list)

        for i in range(n):
            for j in range(m):
                d[matrix[i][j]].append([i, j])

        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]

        for a in sorted(d):
            p = list(range(m + n))
            rank2 = rank[:]
            for i, j in d[a]:
                i, j = find(i), find(j + n)
                p[i] = j
                rank2[j] = max(rank2[i], rank2[j])
            for i, j in d[a]:
                rank[i] = rank[j + n] = matrix[i][j] = rank2[find(i)] + 1
        return matrix