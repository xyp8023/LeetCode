"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        depth = 0;
        if root:
            for i in root.children:
                depth = max(depth, self.maxDepth(i))
            return depth+1
        return 0