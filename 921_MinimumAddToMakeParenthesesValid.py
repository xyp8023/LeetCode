# class Solution:
#     def minAddToMakeValid(self, S):
#         """
#         :type S: str
#         :rtype: int
#         """
#         while '()' in S:
#             S = S.replace('()','')
#         return len(S)


class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        ans = bal = 0
        for symbol in S:
            # if there is a '(' bal+=1, if there is a ')' bal-=1
            bal += 1 if symbol == '(' else -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal


S = '())'
S = '((('
S = '()'
S = "()))(("
S = '(()))'
sol = Solution()
res = sol.minAddToMakeValid(S)
print(res)
