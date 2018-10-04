# class Solution:
#     def hammingDistance(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         x_binary = bin(x).replace('0b','')
#         y_binary = bin(y).replace('0b', '')
#         x_len = len(x_binary)
#         y_len = len(y_binary)
#
#         res = 0
#         max_len = max(x_len, y_len)
#         if x_len==y_len:
#             x_new = x_binary
#             y_new = y_binary
#         else:
#
#             dif_len = abs(x_len - y_len)
#             if x_len==max_len: # x longer than y
#                 y_new = ''
#                 for i in range(dif_len):
#                     y_new+='0'
#                 for i in y_binary:
#                     y_new+=i
#                 x_new = x_binary
#             else: # y longer than x
#                 x_new = ''
#                 for i in range(dif_len):
#                     x_new = x_new + '0'
#                 for i in x_binary:
#                     x_new = x_new + i
#                 y_new = y_binary
#         for i in range(max_len):
#             res+=int(x_new[i])^int(y_new[i])
#         return res


# # other solutions
# # 1.
# class Solution:
#     def hammingDistance(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         x_binary = bin(x)[2:]
#         y_binary = bin(y)[2:]
#         x_len = len(x_binary)
#         y_len = len(y_binary)
#         dif_len = abs(x_len-y_len)
#         res=0
#         # make sure x_bianry always longer
#         if x_len<y_len:
#             x_binary,y_binary = y_binary,x_binary
#         x_len = len(x_binary)
#         y_new = ''
#         y_new = '0' * dif_len
#         y_new += y_binary
#         for i in range(x_len):
#             if x_binary[i]!=y_new[i]:
#                 res+=1
#         return res


# 2.
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_binary = bin(x)[2:]
        y_binary = bin(y)[2:]
        x_len = len(x_binary)
        y_len = len(y_binary)
        res = 0

        # make sure x_bianry always longer
        if x_len < y_len:
            x_binary, y_binary = y_binary, x_binary
            x_len = len(x_binary)
            y_len = len(y_binary)
        if x_len != y_len:
            dif_len = x_len - y_len
            y_new = '0' * dif_len
            y_binary = y_new + y_binary
        for i in range(x_len):
            if x_binary[i] != y_binary[i]:
                res += 1
        return res


x=1
y=4
sol = Solution()
res = sol.hammingDistance(x, y)
print(res)
