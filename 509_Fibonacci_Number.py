class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        zero = 0
        one = 1
        for i in range(1,N):
            zero, one = one, zero + one
        return one


for i in range(9):
    res = Solution().fib(i)
    print(res)
# 0, 1, 1, 2, 3, 5, 8, 13, 21

