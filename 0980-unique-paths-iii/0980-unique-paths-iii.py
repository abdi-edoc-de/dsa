class Solution:
    def dfs(self,i,j,m,n,grid,lst,ei,ej,ct,cnt):
        lst[i][j]=1
        ct+=1
        # print(ct,i,j)
        # print(lst)
        if i==ei and j==ej:
            if ct==cnt:
                # print("ok",ct,cnt)
                # print(lst)
                return 1
            return 0
        row=[-1,1,0,0]
        col=[0,0,-1,1]
        sm=0
        for r in range(4):
            if i+row[r]>=0 and i+row[r]<m and j+col[r]>=0 and j+col[r]<n and grid[i+row[r]][j+col[r]]!=-1 and lst[i+row[r]][j+col[r]]==0:
                sm+=self.dfs(i+row[r],j+col[r],m,n,grid,lst,ei,ej,ct,cnt)
                lst[i+row[r]][j+col[r]]=0
        return sm


    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        hr=0
        m=len(grid)
        n=len(grid[0])
        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==-1:
                    hr+=1
                elif grid[i][j]==1:
                    st=(i,j)
                    cnt+=1
                elif grid[i][j]==2:
                    end=(i,j)
                    cnt+=1
                else:
                    cnt+=1
        lst=[[0]*n for _ in range(m)]
        return self.dfs(st[0],st[1],m,n,grid,lst,end[0],end[1],0,cnt)