# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # d = dict() # Dict[len: int, substr: str]
#         substr = ''
#         N = len(s)
#         max_len = 0
#         for i in range(N):
#             j = i
#             while s[j] not in substr:
#                 substr += s[j]
#                 j+=1
#                 if j>N-1:
#                     break
#             if len(substr)> max_len:
#                 max_len = len(substr)
#                 # d = {max_len: substr}
#             substr = ''
#         return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr, N, max_len = "", 0, 0
        for c in s:
            if c in substr:
                substr = substr[substr.find(c)+1:]
            substr += c
            N = len(substr)
            max_len = N if N > max_len else max_len
        return max_len

s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
sol = Solution()
res = sol.lengthOfLongestSubstring(s)
print(res)