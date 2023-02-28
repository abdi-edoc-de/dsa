class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result , m , n = 0, len(matrix), len(matrix[0])
        def isValid(r, c):
            return 0 <= r < m and 0 <= c < n
        for r in range(m):
            for c in range(n):
                matrix[r][c] = int(matrix[r][c])
                result = max(result, matrix[r][c])
                if not(isValid(r-1, c) and isValid(r, c-1) and isValid(r-1, c-1)):
                    continue
                if matrix[r][c] == 1:
                    matrix[r][c] = 1 + min(matrix[r-1][c], matrix[r][c-1], matrix[r-1][c-1])
                result = max(result , matrix[r][c])
        # for i in matrix:
        #     print(i)
        return result * result