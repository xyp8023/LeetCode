class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        N = len(A)
        for i in A:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        resA = [None]*N
        for i in range(N):
            if i%2==0:
                resA[i]=even[int(i/2)]
            else:
                resA[i]=odd[int(i/2)]
        return resA


A = [4,2,5,7]
A = [1,2,3,4]
sol = Solution()
res = sol.sortArrayByParityII(A)
print(res)
