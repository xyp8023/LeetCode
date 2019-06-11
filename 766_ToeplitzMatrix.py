class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        M = len(matrix)
        N = len(matrix[0])
        if (M == 1) and (N ==1):
            return True
        for i in range(M-1):
            for j in range(N-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True

matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]


sol = Solution()
res = sol.isToeplitzMatrix(matrix)
print(res)