"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            for c in root.children:
                dfs(c)

        res = []
        dfs(root)
        return res