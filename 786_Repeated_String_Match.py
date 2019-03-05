import math

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if B in A:
            return 1
        x = (len(B) // len(A))
        x = math.ceil(len(B) / len(A))
        A_new = A * x
        if B in A_new:
            return x
        else:
            if B in A_new + A:
                return x + 1
            return -1


    def re(self, A, B):
        if B in A:
            return 1
        if (set(B) - set(A))!=set():
            return -1
        A_list = []
        for j in range(1, len(A)+len(B)):
            A_list.append(A*j)
        for item in A_list:
            if B in item:
                return A_list.index(item)+1
        return -1
# A="aaaaaaaaaaaaaaaaaaaaaab"
# B="ba"
# res = Solution().repeatedStringMatch(A, B)
# res1 = Solution().re(A, B)
#
# print(res)
# print(res1)

A = 'abcd'
B='cdabcdab'
res1 = Solution().repeatedStringMatch(A, B)
print(res1)