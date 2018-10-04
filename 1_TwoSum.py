class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # res = [None, None]
        # for i in range(len(nums)):
        #     adder = target - nums[i]
        #     nums_re = list(nums)
        #     nums_re.pop(i)
        #     if adder in nums_re:
        #         index = nums_re.index(adder)
        #         res = [i,index+1]
        #         return res

        res = [None, None]
        for i in range(len(nums)):
            adder = target - nums[i]
            nums_re = list(nums[i+1:])
            if adder in nums_re:
                index = nums_re.index(adder)
                res = [i, index + i+1]
                return res



nums = [3, 2 ,4 ]
# nums = [2, 7, 11, 15]
target = 6
sol = Solution()
res = sol.twoSum(nums, target)
print(res)