class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count=dict()
        for a in  A.split(' '):
            if a not in count:
                count[a]=1
            else:
                count[a]+=1
        for b in B.split(' '):
            if b not in count:
                count[b]=1
            else:
                count[b]+=1
        return [word for word in count if count[word]==1]

A =  "this apple is sweet"
B = "this apple is sour"
sol= Solution()
res=sol.uncommonFromSentences(A, B)
print(res)