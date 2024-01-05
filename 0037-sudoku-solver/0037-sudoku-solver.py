class Solution:
    # def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def solveSudoku(self, grid: List[List[str]]) -> None:
            def is_valid(board, row, col, num):
                # check the number in the row
                for x in range(9):
                    if board[row][x] == num:
                        return False

                # check the number in the column
                for x in range(9):
                    if board[x][col] == num:
                        return False

                # check the number in the box
                start_row, start_col = row - row%3, col - col%3
                for i in range(3):
                    for j in range(3):
                        if board[i+start_row][j+start_col] == num:
                            return False
                return True

            
            def solve(board):
                for i in range(9):
                    for j in range(9):
                        if board[i][j] == ".":
                            for num in "123456789":
                                if is_valid(board, i, j, num):
                                    board[i][j] = num  # attempt to place num in cell

                                    if solve(board):  # proceed to solve the rest
                                        return True

                                    board[i][j] = "."  # undo the current cell for backtracking
                            return False  # trigger backtracking
                return True

            solve(grid)