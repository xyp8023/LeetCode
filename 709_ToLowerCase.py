class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()


str = 'Hello'
# str = 'here'
# str = 'LOVELY'
sol = Solution()
res = sol.toLowerCase(str)
print(res)
