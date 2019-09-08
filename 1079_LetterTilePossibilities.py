from typing import List
from collections import Counter


class Solution:
    # solution 1
    # def numTilePossibilities(self, tiles: str) -> int:
    #     rt_str, tmp_str, counter = [], [], Counter(tiles)
    #     self.backtracking(rt_str,tmp_str, counter, set(tiles))
    #     return len(rt_str)-1
    #
    # def backtracking(self, rt_str: List[str], tmp_str:List[str], counter:Counter, set_tiles:set):
    #     rt_str.append(tmp_str)
    #     for char in set_tiles:
    #         if counter[char]==0:
    #             continue
    #         counter[char]-=1
    #         tmp_str.append(char)
    #         self.backtracking(rt_str, tmp_str, counter, set_tiles)
    #         counter[char]+=1
    #         tmp_str.pop()

    # solution 2
    count = 0
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)
        self.backtracking(counter)
        return self.count

    def backtracking(self, counter:Counter):
        for char in counter:
            if counter[char]>0:
                counter[char]-=1
                self.count+=1
                self.backtracking(counter)
                counter[char]+=1

    # permutation without repeat elements
    def backtrack(self, rlist:List[int], templist:List[int], nums:List[int]):
        # if len(templist) == len(nums):
        rlist.append(templist[:])
        # else:
        for i in nums:
            if i in templist:
                continue
            templist.append(i)
            self.backtrack(rlist, templist, nums)
            templist.pop()

    def permute(self, nums:List[int]):
        rlist = []
        templist = []
        self.backtrack(rlist, templist, nums)
        return rlist

    # permutation with repeat elements
    def backtrack1(self, rlist:List, templist:List, counter:Counter, nums:List[int], length:int):
        # if len(templist) == length:
        rlist.append(templist[:])
        # else:
        for i in nums:
            if counter[i] == 0:
                continue
            counter[i] -= 1
            templist.append(i)
            self.backtrack1(rlist, templist, counter, nums, length)
            counter[i] += 1
            templist.pop()

    def permuteUnique(self, nums):
        rlist, templist, counter = [], [], Counter(nums)
        length = len(nums)
        self.backtrack1(rlist, templist, counter, list(set(nums)), length)
        return rlist


sol = Solution()
nums = [1, 2, 3]
nums_ = [1, 1, 2]
# rlist = sol.permute(nums)
# rtlist = sol.permuteUnique(nums_)
# print(rlist)
# print(rtlist)


tiles = "AAB"
tiles = "AAABBC"
num = sol.numTilePossibilities(tiles)
print(num)
