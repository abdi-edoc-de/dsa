class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        graph = defaultdict(list)
        words.sort(key=len)
        for word in words:
            for i in range(len(word)):
                val = word[:i]+word[i+1:]
                if val in graph:
                    graph[val].append(word)
            graph[word] = []
        # print(graph)
        def dfs(word):
            if word in visited: return visited[word]
            value = 1
            for nei in graph[word]:
                if nei in visited:
                    value = max(value , visited[nei]+1)
                else:
                    value = max(value, dfs(nei)+1)
                    
                    
            visited[word] = value
            return value
        visited = {}
        result = 1
        for word in words:
            if word not in visited:
                result = max(result, dfs(word))
        return result