class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction, heap, n, visited = [(0,1),(0,-1),(1,0),(-1,0), (1,1),(-1,-1),(-1,1),(1,-1)], [], len(grid), set()
        def valid(r,c):
            return 0 <= r < n and 0 <= c < n and grid[r][c] == 0 and  (r,c) not in visited
        if grid[0][0] == 0 and grid[n-1][n-1] == 0:
            heappush(heap, (1, 0,0))
        while heap:
            cost, r, c = heappop(heap)
            if (r,c) == (n-1, n-1): return cost
            for rd, cd in direction:
                nr, nc = r+rd, c + cd
                if not valid(nr, nc):
                    continue
                if (nr, nc) == (n-1, n-1): return cost + 1
                visited.add((nr,nc))
                heappush(heap, (cost+1, nr, nc))
        return -1
                
            
    