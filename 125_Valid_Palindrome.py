# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         for char in s:
#             if not char.isalnum():
#                 s=s.replace(char, '')
#         s=s.upper()
#         print(s)
#         N = len(s)
#         for i in range(N // 2):
#             if s[i] != s[N - 1 - i]:
#                 return False
#         return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        left = 0
        right = N-1
        while left<right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[left].upper()!=s[right].upper():
                return False
            left+=1
            right-=1
        return True

s = "A man, a plan, a canal: Panama"
# s ="race a car"
print(Solution().isPalindrome(s))
