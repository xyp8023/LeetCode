class Solution:
    def projectionArea(self, grid):
        a = sum(map(max, grid))
        # a = sum(map(lambda x: max(x), [x for x in grid]))

        b = sum(map(max, zip(*grid)))
        # b = sum(map(lambda x: max(x), [x for x in zip(*grid)]))

        c = sum(v > 0 for row in grid for v in row)
        # c = sum(map(lambda x: x>0,[x for row in grid for x in row]))
        return a+b+c



grid = [[1,2,3,4],[5,6,7,8],[1+8,2+8,3+8,4+8],[5+8,6+8,7+8,8+8]]
# grid = [[1,0],[0,2]]
sol = Solution()
res = sol.projectionArea(grid)
print(res)