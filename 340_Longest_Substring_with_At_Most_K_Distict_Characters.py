from typing import List

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:
            return 0
        right, max_len = 0, 0
        N = len(s)
        for idx in range(N):
            while right < N:
                if len(set(s[idx:right])) <= k:
                    right+=1
                else:
                    max_len = max(max_len, len(s[idx:right-1]))
                    break
            if right == N:
                max_len = max(max_len, len(s[idx:right])) if len(set(s[idx:right])) <= k else max(max_len, len(s[idx:right - 1]))
        return max_len


s = "eceba"
k = 2
# s = 'aa'
# k=1
s = 'ab'
k=1
print(Solution().lengthOfLongestSubstringKDistinct(s, k))