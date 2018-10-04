class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if len(moves) < 2:
            return False

        if moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D'):
            return True
        else:
            return False


# # another solution
# class Solution:
#     def judgeCircle(self, moves):
#         """
#         :type moves: str
#         :rtype: bool
#         """
#         x = 0
#         y = 0
#         for i in moves:
#             if i == 'R':
#                 x += 1
#             elif i == 'L':
#                 x -= 1
#             elif i == 'U':
#                 y += 1
#             elif i == 'D':
#                 y -= 1
#         return x == 0 and y == 0


moves= 'UD'
# moves = 'LL'
sol = Solution()
res = sol.judgeCircle(moves)
print(res)