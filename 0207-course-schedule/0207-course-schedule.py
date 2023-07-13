class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, income = defaultdict(list), defaultdict(int)
        count = 0
        for frm, to in prerequisites:
            graph[to].append(frm)
            income[frm] += 1
        que = deque()
        for key in range(numCourses):
            if income[key] == 0:
                que.append(key)
        while que:
            count += 1
            course = que.popleft()
            for nei in graph[course]:
                income[nei] -= 1
                if income[nei] == 0:
                    que.append(nei)
        return count == numCourses
    
                