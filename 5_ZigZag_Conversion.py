# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         lst = []
#         N = len(s)
#         print (N//(2*numRows-2))
#         [lst.append([s[i]]) for i in range(numRows)]
#         step = 2*numRows-2
#         for k in range(N//step):
#             if k:
#                 [lst[i].append(s[k * step + i]) for i in range(numRows)]
#             [lst[i].append(s[k*step+numRows-1-i+numRows-1]) for i in range(numRows-2,0, -1)]
#         for k in range(N%step):
#             lst[k].append(s[N//step *step + k])
#         return lst



# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         lst = []
#         N = len(s)
#         if numRows == 1 or N <= 2 or numRows >= N:
#             return s
#         # print (N//(2*numRows-2))
#         [lst.append(s[i]) for i in range(numRows)]
#         step = 2*numRows-2
#         if N < step:
#             for i in range(numRows-2, 2, -1):
#                 # j = i
#                 # a = numRows-1-i + numRows-1
#                 lst[i] += (s[numRows-1-i + numRows-1])
#         for k in range(N//step):
#             if k:
#                 for i in range(numRows):
#                     lst[i]+=(s[k * step + i])
#             for i in range(numRows - 2, 0, -1):
#                 lst[i]+=(s[k*step+numRows-1-i+numRows-1])
#         if N > step:
#             for k in range(min(N%step, numRows)):
#                 a = N//step *step + k
#                 lst[k]+=(s[N//step *step + k])
#             if N%step - numRows>0:
#                 for i in range(N%step - numRows):
#                     lst[numRows-i-2]+=s[N//step *step + numRows+i]
#
#
#         return "".join(lst)
#
#








class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lst, idx = [], 0
        p_down, p_up = 0, numRows-2  # p_down [0,numRows-1], p_up [numRows-2,1]
        N = len(s)
        if numRows == 1 or N <= 2 or numRows >= N:
            return s
        [lst.append(s[i]) for i in range(numRows)]
        idx += numRows
        while idx < N:
            if p_up <= 1:
                p_up = numRows-2
            if p_down >= numRows-1:
                p_down = 0
            while p_up >= 1:
                if idx >= N:
                    break
                lst[p_up] += s[idx]
                p_up -= 1
                idx += 1
            while p_down <= numRows-1:
                if idx >= N:
                    break
                lst[p_down] += s[idx]
                p_down += 1
                idx += 1


        return "".join(lst)
s = "PAYPALISHIRINGXYZU"
# s = "PAYPALISHIRING"
numRows = 5
sol = Solution()
print(sol.convert(s, numRows))