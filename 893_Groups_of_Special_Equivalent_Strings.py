class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        d = dict()
        for i in A:
            if len(i)>=2:
                x = tuple(sorted(i[::2]))
                y = tuple(sorted(i[1::2]))
                key = (tuple(sorted(i[::2])),tuple(sorted(i[1::2])))
                d[key] = d.get(key,0)+1
            else:
                d[i] = d.get(i,0)+1
        return len(d)


A = ["a","b","c","a","c","c"]  # output = 3
A = ["aa","bb","ab","ba"]  # output = 4
A = ["abc","acb","bac","bca","cab","cba"]  # output = 3
A = ["abcd","cdab","adcb","cbad"]  # output = 1
sol = Solution()
res = sol.numSpecialEquivGroups(A)
print(res)