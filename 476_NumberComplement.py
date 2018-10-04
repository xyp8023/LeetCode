class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bi_num = format(num, 'b')
        # bi_num =list(bin(num)[2:])
        com_num = ''
        for bit in bi_num:
            if bit=='0':
                com_num+='1'
            else:
                com_num += '0'
        return int(com_num, 2)


# other solutions
# 1.
# import math
# class Solution:
#     def findComplement(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         return pow(2,math.floor(math.log2(num))+1)-1-num


# 2.
# class Solution(object):
#     def findComplement(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         n = 1
#         while n <= num:
#             n <<= 1
#         return (n - 1) ^ num


num = 5
num = 1
sol = Solution()
res = sol.findComplement(num)
print(res)