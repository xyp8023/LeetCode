class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        D = 0
        Matrix = list(zip(*A))
        for columns in Matrix:
            if sorted(list(columns)) != list(columns):
                D+=1

        return D

A = ["cba","daf","ghi"]
# A = ["a","b"]
# A = ["zyx","wvu","tsr"]
sol = Solution()
res = sol.minDeletionSize(A)
print(res)