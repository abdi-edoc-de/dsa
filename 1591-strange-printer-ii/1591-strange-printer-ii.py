
from collections import defaultdict, deque

class Solution:
    def isPrintable(self, mat):
        n, m = len(mat), len(mat[0])
        dp = defaultdict(list)
        ind = [0] * 65
        uni = set()

        for i in range(n):
            for j in range(m):
                uni.add(mat[i][j])

        for it in uni:
            min_x = min_y = float('inf')
            max_x = max_y = float('-inf')

            for i in range(n):
                for j in range(m):
                    if mat[i][j] == it:
                        min_x = min(min_x, i)
                        max_x = max(max_x, i)
                        min_y = min(min_y, j)
                        max_y = max(max_y, j)

            if min_x == float('inf'):
                continue

            d = set()
            for i in range(min_x, max_x + 1):
                for j in range(min_y, max_y + 1):
                    if mat[i][j] != it:
                        d.add(mat[i][j])

            for t in d:
                dp[it].append(t)
                ind[t] += 1

        q = deque()
        for it in uni:
            if ind[it] == 0:
                q.append(it)

        count = 0
        while q:
            temp = q.popleft()
            count += 1
            for it in dp[temp]:
                ind[it] -= 1
                if ind[it] == 0:
                    q.append(it)

        return count == len(uni)
