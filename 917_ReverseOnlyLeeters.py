class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S_NotLetters = {}
        S_Letters = []
        N = len(S)
        res_S = ''
        for i in range(N):
            if S[i].isalpha():
                S_Letters.append(S[i])
            else:
                S_NotLetters[i] = S[i]
        a = list(S_NotLetters.keys())
        for i in range(N):
            if i in a:
                res_S += S_NotLetters[i]
            else:

                res_S+= S_Letters.pop()
        return res_S


# other solutions
# class Solution(object):
#     def reverseOnlyLetters(self, S):
#         S = list(S)
#         left, right = 0, len(S)-1
#         while left < right:
#             while not S[left].isalpha() and left < right:
#                 left += 1
#             while not S[right].isalpha() and left < right:
#                 right -= 1
#             if S[left].isalpha() and S[right].isalpha() and left < right:
#                 S[left], S[right] = S[right], S[left]
#                 left += 1
#                 right -= 1
#         return ''.join(S)


S = "a-bC-dEf-ghIj"
sol = Solution()
res = sol.reverseOnlyLetters(S)
print(res)

