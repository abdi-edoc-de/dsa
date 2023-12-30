class Solution:
    def __init__(self):
        self.dp = []
    
    def minNumberOfSemesters(self, n, relations, k):
        indegree = [0] * n
        adj = [[] for _ in range(n)]

        # Counting indegree and storing neighbors
        for i in relations:
            indegree[i[1] - 1] += 1
            adj[i[0] - 1].append(i[1] - 1)

        # Setting all n bits to 1
        mask = (1 << n) - 1
        self.dp = [-1] * (mask + 1)

        return self.solve(mask, indegree, adj, k)
    
    def solve(self, mask, indegree, adj, k):
        if mask == 0:
            return 0
        if self.dp[mask] != -1:
            return self.dp[mask]

        ans = float('inf')
        # Get the nodes which are eligible (1 bit) and indegree = 0
        nodes = [i for i in range(len(indegree)) if mask & (1 << i) and indegree[i] == 0]
        val = len(nodes)
        combinations = self.uniqueCombinations(nodes, min(val, k))

        for i in combinations:
            new_mask = mask
            new_indegree = indegree.copy()

            for j in i:
                new_mask ^= (1 << j)
                for child in adj[j]:
                    new_indegree[child] -= 1
            
            ans = min(ans, 1 + self.solve(new_mask, new_indegree, adj, k))

        self.dp[mask] = ans
        return ans

    def generateCombinations(self, nodes, k, start_index, current_combination, result):
        if k == 0:
            result.append(current_combination[:])
            return

        for i in range(start_index, len(nodes)):
            current_combination.append(nodes[i])
            self.generateCombinations(nodes, k - 1, i + 1, current_combination, result)
            current_combination.pop()

    def uniqueCombinations(self, nodes, k):
        result = []
        current_combination = []
        self.generateCombinations(nodes, k, 0, current_combination, result)
        return result
