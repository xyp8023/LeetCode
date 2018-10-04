class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A_new = sorted(A)
        return A.index(A_new[-1])


# # other solutions
# # 1.
# class Solution:
#     def peakIndexInMountainArray(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         for i in range(len(A)-1):
#             if A[i]>A[i+1]:
#                 return i
#
#
#
# # 2. binary search
# class Solution:
#     def peakIndexInMountainArray(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         l=0
#         r=len(A)-1
#         while l<r:
#             mid = int((l+r)/2)
#             if A[mid-1]>A[mid]:
#                 r = mid
#             elif A[mid]<A[mid+1]:
#                 l = mid
#             else:
#                 return mid
#
#
# # 3. one line python
# class Solution:
#     def peakIndexInMountainArray(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         return A.index(max(A))


A = [0, 1, 0]
A = [0, 2, 1, 0]
sol = Solution()
res = sol.peakIndexInMountainArray(A)
print(res)