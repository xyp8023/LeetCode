class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for char in s:
            if char not in d:
                d[char]=1
            else:
                d[char]+=1
        for key, value in d.items():
            if value==1:
                return s.index(key)
        return -1
