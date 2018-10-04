class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(zip(*A))


A = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
res = sol.transpose(A)
print(res)
# = res = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]