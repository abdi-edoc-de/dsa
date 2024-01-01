
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        empty = 0  # Count the number of empty squares
        m, n = len(grid), len(grid[0])
        
        # Find the start and end position, and count the non-obstacle squares
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx, sy = i, j
                elif grid[i][j] == 2:
                    ex, ey = i, j
                if grid[i][j] != -1:
                    empty += 1

        # DFS function
        def dfs(x, y, count):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == -1:
                return  # If out of bounds or hits an obstacle, stop
            if x == ex and y == ey:
                if count == empty:
                    self.ans += 1  # Found a valid path
                return
            grid[x][y] = -1  # Mark the square as visited
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Explore four directions
                dfs(x + dx, y + dy, count + 1)
            grid[x][y] = 0  # Backtrack

        dfs(sx, sy, 1)
        return self.ans
