class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:

        graph = defaultdict(set)
        for a,b in pairs:
            graph[a].add(b)
            graph[b].add(a)

        res = []
        visited = set()
        for node in graph:
            if len(graph[node]) == 1:
                res.append(node)
                visited.add(node)
                break
        
        n = len(pairs)  + 1
        while len(res) < n:
            for node in graph[res[-1]]:
                if node not in visited:
                    res.append(node)
                    visited.add(node)
                    break
        
        return res