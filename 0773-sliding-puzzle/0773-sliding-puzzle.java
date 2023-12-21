
class Solution {
    private HashMap<String, Integer> memo;

    public Solution() {
        this.memo = new HashMap<>();
    }

    public int slidingPuzzle(int[][] board) {
        String initialState = getState(board);

        Queue<String> q = new ArrayDeque<>();
        q.offer(initialState);

        int dist = 0;
        HashSet<String> vis = new HashSet<>();

        while (!q.isEmpty()) {
            int levelLen = q.size();
            for (int i = 0; i < levelLen; i++) {
                String state = q.poll();
                if (state.equals("123450")) {
                    return dist;
                }

                int[] zxzy = setState(state, board);
                int zx = zxzy[0], zy = zxzy[1];

                for (int[] dir : new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}) {
                    int x = zx + dir[0], y = zy + dir[1];
                    if (0 <= x && x < 2 && 0 <= y && y < 3) {
                        swap(board, zx, zy, x, y);
                        String newState = getState(board);
                        if (!vis.contains(newState)) {
                            vis.add(newState);
                            q.offer(newState);
                        }
                        swap(board, zx, zy, x, y); // Swap back
                    }
                }
            }
            dist++;
        }

        return -1;
    }

    private String getState(int[][] board) {
        StringBuilder sb = new StringBuilder();
        for (int[] row : board) {
            for (int x : row) {
                sb.append(x);
            }
        }
        return sb.toString();
    }

    private int[] setState(String state, int[][] board) {
        int si = 0, zx = 0, zy = 0;
        for (int row = 0; row < 2; row++) {
            for (int i = 0; i < 3; i++) {
                board[row][i] = state.charAt(si) - '0';
                if (board[row][i] == 0) {
                    zx = row;
                    zy = i;
                }
                si++;
            }
        }
        return new int[]{zx, zy};
    }

    private void swap(int[][] board, int x1, int y1, int x2, int y2) {
        int temp = board[x1][y1];
        board[x1][y1] = board[x2][y2];
        board[x2][y2] = temp;
    }

}

