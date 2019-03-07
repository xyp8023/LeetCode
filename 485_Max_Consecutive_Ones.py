from typing import List


class Solution:
#     def findMaxCosecutiveOnes(self, nums: List[int]) -> int:
#         N = len(nums)
#         len_ones_lst = []
#         left = 0
#         cnt=0
#         while left < N-1:
#             if nums[left]:
#                 cnt+=1
#             else:
#                 len_ones_lst.append(cnt)
#                 cnt=0
#                 left+=1
#         return max(len_ones_lst)
#
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         str_nums = ''.join(str(num) for num in nums)
#         sep_str_nums = str_nums.split('0')
#         max_len = 0
#         for ones in sep_str_nums:
#             max_len = max(max_len, len(ones))
#         return max_len
#
#
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         N = len(nums)
#         max_ones = 0
#         cnt = 0
#         for num in nums:
#             if num:
#                 cnt+=1
#                 max_ones = max(max_ones, cnt)
#             else:
#                 cnt=0
#         return max_ones

    def removeDuplicates(self, A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]
        print(A)
        return newTail + 1

nums = [0,0,1,1,1,2,2,3,3,4]
print (Solution().removeDuplicates(nums))