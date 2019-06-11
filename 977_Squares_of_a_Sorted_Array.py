from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        rA = [0] * len(A)
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                rA[r - l] = left * left
                l += 1
            else:
                rA[r - l] = right * right
                r -= 1
            print (rA)
        return rA


A = [-4,-1,0,3,10]
res = Solution().sortedSquares(A)
print(res)
