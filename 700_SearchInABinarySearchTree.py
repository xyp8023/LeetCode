# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def searchBST(self, root, val):
#         """
#         :type root: TreeNode
#         :type val: int
#         :rtype: TreeNode
#         """
#         if root==None:
#             return root
#         elif root.val==val:
#             return root
#         else:
#             r_res = self.searchBST(root.left, val)
#             if r_res==None:
#                 r_res=self.searchBST(root.right, val)
#             return r_res


# another solution
class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        rNode = [None]

        def dfs(Node):
            if Node==None:
                return
            if Node.val == val:
                rNode[0]=Node
            dfs(Node.left)
            dfs(Node.right)
        dfs(root)
        return rNode[0]




