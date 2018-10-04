class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_A = []
        odd_A  = []
        for i in A:
            if i%2:
                odd_A.append(i)
            else:
                even_A.append(i)
        return even_A+odd_A


# # other solutions
# # 1. idea: if odd is on the left and even is on the right, then swap
# class Solution:
#     def sortArrayByParity(self, A):
#         """
#         :type A: List[int]
#         :rtype: List[int]
#         """
#         start, end = 0, len(A) - 1
#         while start < end:
#             m, n = A[start], A[end]
#             if m % 2 == 1 and n % 2 == 0:
#                 A[start], A[end] = n, m
#             elif m % 2 == 1:
#                 end -= 1
#             elif n % 2 == 0:
#                 start += 1
#             else:
#                 start += 1
#                 end -= 1
#         return A


# # 2. using sorted function with the key parity
# class Solution:
#     def sortArrayByParity(self, A):
#         """
#         :type A: List[int]
#         :rtype: List[int]
#         """
#         return sorted(A,key = lambda x:x%2)


A= [3, 1, 2, 4]
sol = Solution()
res = sol.sortArrayByParity(A)
print(res)

