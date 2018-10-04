# class Solution:
#     def selfDividingNumbers(self, left, right):
#         """
#         :type left: int
#         :type right: int
#         :rtype: List[int]
#         """
#         num_list = list(range(left, right + 1))
#         res = []
#         for i in num_list:
#             if '0' in str(i):
#                 continue
#             else:
#                 n = len(str(i))
#                 flag = True
#                 if n==1:
#                     res.append(i)
#                 else:
#                     for j in range(n):
#                         div = int(str(i)[j])
#                         if div==1:
#                             continue
#                         else:
#                             if i % div!=0:
#                                 flag = False
#                     if flag:
#                         res.append(i)
#         return res


# other solutions
# 1.
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right+1):
            falg = True
            for j in str(i):
                if int(j)==0 or i%int(j)!=0:
                    falg=False
            if falg:
                res.append(i)
        return res

# # 2.
# class Solution:
#     def selfDividingNumbers(self, left, right):
#
#         # return [x for x in range(left, right + 1) if all([int(i) != 0 and x % int(i) == 0 for i in str(x)])]
#         return [x for x in range(left, right + 1) if all((i and (x % i == 0) for i in map(int, str(x))))]
#

left = 1
right = 22
sol = Solution()
res = sol.selfDividingNumbers(left, right)
print(res)