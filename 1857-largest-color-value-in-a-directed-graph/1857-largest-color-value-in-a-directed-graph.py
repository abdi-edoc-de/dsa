class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        indegree, graph, result = defaultdict(int), defaultdict(list) ,0
        start = set()
        if not edges:
            return 1
        for frm, to in edges:
            indegree[to] += 1
            graph[frm].append(to)
            if indegree[frm] == 0:
                start.add(frm)
            if to in start:
                start.remove(to)
        dp = {}
        check = [False]
        def dfs(node, prevs):
            if check[0]: return [0]
            if node in dp:
                return dp[node]
            arr = [0] * 26
            for nei in graph[node]:
                if nei in prevs:
                    check[0] = True
                    return [0]
                prevs.add(nei)
                c = dfs(nei, prevs)
                prevs.remove(nei)
                for i, item in enumerate(c):
                    arr[i] = max(arr[i], item)
            arr[ord(colors[node]) - ord('a')] += 1
            dp[node] = arr
            return arr
        for node in start:
            result = max(result, max(dfs(node, set([node]))))
        if check[0] or not start: return -1
        return result
            
        
            
        
        
        