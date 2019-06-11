class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        find_all = lambda c, s: [x for x in range(c.find(s), len(c)) if c[x] == s]
        rS = list()
        index_zero = find_all(S, C)
        for i in range(len(S)):
            dis = [abs(x-i) for x in index_zero]
            rS.append(min(dis))
        return rS


S = 'loveleetcode'
C = 'e'
sol = Solution()
res=sol.shortestToChar(S,C)
print(res)