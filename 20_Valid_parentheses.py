# class Solution:
    # def isValid(self, s: str) -> bool:
    #     N = len(s)
    #     if N%2==1:
    #         return False
    #     if s.count('(')!=s.count(')') or s.count('[')!=s.count(']') or s.count('{')!=s.count('}'):
    #         return False
    #     while ((len(s)>0) and ('()' in s or '[]' in s or '{}' in s)):
    #         s = s.replace('()', '')
    #         s = s.replace('[]', '')
    #         s = s.replace('{}', '')
    #     return True if len(s)==0 else False

class Solution:
    def isValid(self, s: str) -> bool:
        N = len(s)
        if N % 2 == 1:
            return False
        if s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):
            return False
        d = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in d:
                stack.append(d[char])
            elif not stack or char != stack.pop():
                return False
        return True


s = '['
print(Solution().isValid(s))