class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)/2
        return sum(nums[::2])


nums = [1, 4, 3, 2]
sol = Solution()
res = sol.arrayPairSum(nums)
print(res)