class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # N = len(S)
        # rList = []
        # sList = list(range(0,N+1))
        # for i in range(0, N):
        #     if S[i]=='I':
        #         rList.append(sList.pop(0))
        #     else:
        #         rList.append(sList.pop(-1))
        # rList.append(sList.pop(0))
        #
        # return rList

        N = len(S)
        rList = []
        k, j = 0, N
        for i in range(0,N):
            if S[i]=='I':
                rList.append(k)
                k+=1
            else:
                rList.append(j)
                j-=1
        rList.append(k)
        return rList


# S = 'IDID'
# S = 'III'
S = 'DDI'
sol = Solution()
res = sol.diStringMatch(S)
print(res)