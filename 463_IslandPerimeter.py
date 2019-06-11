class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = {0:0, 1:0, 2:0, 3:0,4:0}
        M = len(grid)
        N = len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j]==1:
                    res = self.surroundOnesNum(grid, i, j, M, N)
                    count[res]+=1
        return (count[1]*3) + (count[2]*2) +(count[3]*1)+(count[0]*4)
    def surroundOnesNum(self,grid, i, j,M,N):
        res=0

        if 0<=i-1<M:
            res+=grid[i-1][j]
        if 0<=i+1<M:
            res+=grid[i+1][j]
        if 0<=j-1<N:
            res+=grid[i][j-1]
        if 0 <= j + 1 < N:
            res += grid[i][j + 1]
        return res

grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
grid = [[1,0]]
sol = Solution()
res = sol.islandPerimeter(grid)
print(res)