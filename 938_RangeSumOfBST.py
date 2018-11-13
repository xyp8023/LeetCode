# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.res = 0

        def dfs(self, root):
            if root == None:
                return
            else:
                if L <= root.val <= R:
                    self.res += root.val
            dfs(self, root.left)
            dfs(self, root.right)


        dfs(self, root)
        return self.res


