# class Solution:
#     def flipAndInvertImage(self, A):
#         """
#         :type A: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         len_a = len(A[0])
#         A_new = []
#         for a in A:
#             a_new = []
#             for i in range(len_a):
#                 x =a[len_a-1-i] ^ 1
#                 a_new.append(x)
#             A_new.append(a_new)
#         return A_new


# 1 line python
class Solution:
    def flipAndInvertImage(self, A):
        return [[1 ^ i for i in row[::-1]] for row in A]


# A = [[1,1,0],[1,0,1],[0,0,0]]
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
sol = Solution()
res = sol.flipAndInvertImage(A)
print(res)

