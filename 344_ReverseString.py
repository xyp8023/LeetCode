class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        List_s = list(s)
        List_s.reverse()
        for i in List_s:
            res+=i
        return res

s = 'hello'
sol = Solution()
res = sol.reverseString(s)
print(res)