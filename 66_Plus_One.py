from typing import List

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         N = len(digits)
#         num=0
#         for i in range(N):
#             num+=digits[N-1-i]*(10**i)
#         num +=1
#         # rDigits = [0] * (N+1)
#         rDigits = []
#         print(num)
#         for i in str(num):
#             rDigits.append(int(i))
#         return rDigits

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        num=''
        for i in digits:
            num+=str(i)
        num = str(int(num)+1)
        print(num)
        rDigits=[]
        for i in num:
            rDigits.append(int(i))
        return rDigits
digits = [9]
digits = [9,9,9]
print(Solution().plusOne(digits))
