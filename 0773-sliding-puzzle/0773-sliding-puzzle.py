class Solution:
    def __init__(self):
        self.memo = dict()
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def getState(board):
            return ''.join(str(x) for row in board  for x in row)
        
        # print(getState(board))
        
        def setState(state):
            si = 0
            zx, zy = 0, 0
            for row in range(2):
                for i in range(3):
                    board[row][i] = int(state[si])
                    if board[row][i] == 0:
                        zx,zy = row, i
                    si += 1
                    
            # returns the position of zero ;)
            return zx, zy
        
        # now BFS
        q = deque([getState(board)])
        dist = 0
        vis = set()
        
        while q:
            # print(q)
            level_len = len(q)
            for _ in range(level_len):
                if q[0] == '123450':
                    return dist
                zx, zy = setState(q.popleft())
                # now check all four neighbours.. after swap what happens :)
                for x, y in [[zx,zy+1], [zx+1,zy],[zx,zy-1],[zx-1,zy]]:
                    if 0<=x<2 and 0<=y<3:
                        board[zx][zy], board[x][y] = board[x][y], board[zx][zy]
                        state = getState(board)
                        if state not in vis:
                            vis.add(state)
                            q.append(state)
                        board[zx][zy], board[x][y] = board[x][y], board[zx][zy]
            dist += 1
        
        return -1