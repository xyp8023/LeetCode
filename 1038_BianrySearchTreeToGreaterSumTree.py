# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    seen = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right:
            self.bstToGst(root.right)
        self.seen += root.val
        root.val = self.seen
        if root.left:
            self.bstToGst(root.left)
        return root
