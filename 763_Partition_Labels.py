class Solution:
    def __init__(self):
        self.res = []

    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        if len(S) == 1:
            self.res.append(1)
            
        def overlap_or_not(left, right):
            flag = False
            for r_str in right:
                if r_str in left:
                    flag = True
                    break
            return flag
        for i in range(1, n):
            left = S[:i]
            right = S[i:]
            flag = overlap_or_not(left, right)
            if not flag:
                self.res.append(len(left))
                self.partitionLabels(right)
                break
            if i == n-1:
                self.res.append(n)
        return self.res


S = "ababcbacadefegdehijhklij"
S = "eaaaabaaec"
sol = Solution()
res = sol.partitionLabels(S)
print(res)
