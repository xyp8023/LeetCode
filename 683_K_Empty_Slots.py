from typing import List

#
# class Solution:
#     def kEmptySlots(self, flowers: List[int], k: int) -> int:
#
#         blooming_flowers = [0] * len(flowers)
#         for i in range(len(flowers)):
#             blooming_flowers[flowers[i]-1] = 1
#             if self.check(blooming_flowers, k):
#                 return i + 1
#         return -1
#
#     def check(self, blooming_flowers, k):
#         a = [0] * k
#         aaa = '1'+ ''.join(str(x) for x in a)+'1'
#         bbb = ''.join(str(x) for x in blooming_flowers)
#         return aaa in bbb
class Solution:
    def kEmptySlots(self, flowers: List[int], k: int) -> int:
        from bisect import bisect, insort
        indices = [flowers[0]]
        for idx in range(1, len(flowers)):
            index = bisect(indices, flowers[idx])
            insort(indices, flowers[idx])
            if (index!=0 and indices[index]-indices[index-1]==k+1) or (index!=len(indices)-1 and indices[index+1]-indices[index]==k+1):
                return idx+1
        return -1
# flowers = [1, 3, 2]
# k=1
# flowers = [1, 2, 3]
# k =1
flowers = [6,5,8,9,7,1,10,2,3,4]
k = 2
res = Solution().kEmptySlots(flowers, k)
print(res)