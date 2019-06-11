class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # the possible smallest max(B) is max(A)-K
        # the possible largest min(B) is min(B)+K
        # if the difference between them is smaller than 0, then return 0
        # otherwise return the difference
        return max(0, max(A)-2*K-min(A))
A = [1, 3, 6]
K = 3
sol = Solution()
res = sol.smallestRangeI(A, K)
print(res)