class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # skyline viewed from top or bottom
        res = 0
        row_max = [max(x) for x in grid]
        col_max = [max(x) for x in zip(*grid)]
        for i in range(len(row_max)):
            for j in range(len(col_max)):
                res += min(row_max[i], col_max[j])
                res -= grid[i][j]
        return res


grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
sol = Solution()
res = sol.maxIncreaseKeepingSkyline(grid)
print(res)