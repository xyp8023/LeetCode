class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        max_nums = max(nums)
        rTreeNode = TreeNode(max_nums)
        left_nums = nums[:nums.index(max_nums)]
        right_nums = nums[nums.index(max_nums)+1:]
        if left_nums:
            rTreeNode.left = self.constructMaximumBinaryTree(left_nums)
        if right_nums:
            rTreeNode.right = self.constructMaximumBinaryTree(right_nums)

        return rTreeNode



