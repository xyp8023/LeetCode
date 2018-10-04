class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        for j in J:
            if j in S:
                res += S.count(j)
        return res


J = 'aA'
S = 'aAAbbbb'
# J = 'z'
# S = 'ZZ'
sol = Solution()
res = sol.numJewelsInStones(J, S)
print(res)