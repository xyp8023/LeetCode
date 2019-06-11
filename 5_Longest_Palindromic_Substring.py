# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def ifPalindrome(s):
#             return s==s[::-1]
#         N, max_len = len(s), 0
#         if N<=1:
#             return s
#         res_str = ""
#         # while left < N-max_len:
#         for left in range(N-max_len):
#             right = N-1
#             while right-left>=max_len:
#                 cur_str = s[left:right+1]
#                 if ifPalindrome(cur_str):
#                     max_len = len(cur_str)
#                     res_str = cur_str
#                 else:
#                     right-=1
#             left+=1
#         return res_str
# DP
class Solution:
    def findMaxLen(self, s):
        def ifPalindrome(s):
            return s == s[::-1]
        substr = s
        max_len = 0
        if not ifPalindrome(substr):
            # max_len = self.longestPalindrome(substr[1:])
            if substr in self.d:
                return self.d[substr]
            else:
                left = self.findMaxLen(substr[1:])
                right = self.findMaxLen(substr[:-1])
                max_len = max(left,right)
                self.d[substr] = max_len
        else:
            max_len = max(len(substr), max_len)
            self.d[substr] = max_len
            self.d1[max_len] = substr
        return max_len
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        self.d = dict()
        self.d1 = dict()
        substr = ""
        for c in s:
            substr+=c
            max_len = self.findMaxLen(substr)
        for key, value in self.d.items():
            if value == max_len:
                return self.d1[value]

s = "bb"
# s = "jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"
sol = Solution()
res = sol.longestPalindrome(s)
print(res)