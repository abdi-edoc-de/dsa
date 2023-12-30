class Solution:
    def __init__(self):
        self.mod = 10**9 + 7
        self.DX = [-1, 1, 0, 0]
        self.DY = [0, 0, -1, 1]
        
    def func(self, grid, dp, x, y, m, n):
        seju = 1
        
        # Check if the result for the current position is already calculated
        if dp[x][y] != -1:
            return dp[x][y]
        
        # Iterate over the neighboring cells
        for i in range(4):
            cx = x + self.DX[i]
            cy = y + self.DY[i]
            
            # Check if the neighboring cell is within the grid boundaries and has a greater value
            if 0 <= cx < m and 0 <= cy < n and grid[x][y] < grid[cx][cy]:
                seju += self.func(grid, dp, cx, cy, m, n)
        
        # Store the calculated result in the dp array for future reference
        dp[x][y] = seju % self.mod
        return dp[x][y]
    
    def countPaths(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        # Create a dp array to store the intermediate results
        dp = [[-1] * n for _ in range(m)]
        
        seju = 0
        
        # Iterate over all cells in the grid
        for i in range(m):
            for j in range(n):
                # Calculate the number of paths starting from each cell
                seju += self.func(grid, dp, i, j, m, n)
        
        # Return the total number of paths modulo 10^9 + 7
        return seju % self.mod
