# class Solution:
#     def myAtoi(self, str):
#         flag = 1
#         if len(str) == 0:
#             return 0
#         if str[0].isnumeric() or str[0]==" " or str[0]=="+" or str[0]=="-":
#             str = str.lstrip(" ")
#             if str == "+" or str=="-" or len(str) == 0:
#                 return 0
#             if str[0]=="-":
#                 flag = -1
#                 str = str.lstrip("-")
#             elif str[0]=="+":
#                 str = str.lstrip("+")
#             if not str[0].isnumeric():
#                 return 0
#             str1 = ""
#             for c in str:
#                 if c.isnumeric():
#                     str1+=c
#                 else:
#                     break
#             num = int(str1)
#             if flag==1:
#                 if num >= 2**31:
#                     num = 2**31-1
#             else:
#                 if num > 2**31:
#                     num = 2**31
#             return flag*num
#         else:
#             return 0


class Solution:
    def myAtoi(self, str):
        Minusflag = False
        if len(str) == 0:
            return 0
        if str[0] == " ":
            str = str.lstrip(" ")
            if len(str) == 0:
                return 0
        if str[0].isnumeric():
            pass
        elif str[0] == "+":
            str = str[1:]
        elif str[0] == "-":
            str = str[1:]
            Minusflag = True
        else:
            return 0
        str1 = ""
        for c in str:
            if c.isnumeric():
                str1+=c
            else:
                break
        if len(str1) == 0:
            return 0
        else:
            num = int(str1)
        if not Minusflag:
            if num >= 2 ** 31:
                num = 2 ** 31 - 1
        else:
            if num > 2 ** 31:
                num = 2 ** 31
        return   -num if Minusflag else num

str = "   -42"
str = "42"
str = "4193 with words"
str = "words and 987"
str = "-91283472332"
str = "+"
str = "+1"

str = " ++1"
str = " "
str = " -"
str = "+-2"
str = " b11228552307"
str = "-+1"
sol = Solution()
res = sol.myAtoi(str)
print(res)