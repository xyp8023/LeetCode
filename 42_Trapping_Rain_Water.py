from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        h, left, right, water = [], 0, 0, 0
        for i in height:
            left = max(left, i)
            h.append(left)
        h.reverse()
        r = []
        for idx, cur_height in enumerate(reversed(height)):
            right = max(right, cur_height)
            r.append(right)
            water += min(h[idx], right) - cur_height
        return water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))
