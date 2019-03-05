# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        longest=[0]
        def traverse(node):
            if not node:
                return 0
            left_len, right_len = traverse(node.left), traverse(node.right)
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            longest[0] = max(longest[0], left + right)

            print('left',left)
            print('right', right)
            print('longest', longest)
            return max(left, right)

        traverse(root)
        return longest[0]

        # NodeDigits = dict()
        #
        # def find(node, NodeDigits):
        #     if not node.val:
        #         return
        #     if (node.left is not None):
        #         if (node.left.val == node.val):
        #             if node.val not in NodeDigits:
        #                 NodeDigits[node.val] = (1,1)
        #             if node.val in NodeDigits:
        #                 NodeDigits[node.val] += (0,1)
        #
        #     if (node.right is not None ):
        #         if (node.right.val == node.val):
        #             if node.val not in NodeDigits:
        #                 NodeDigits[node.val] = (1,1)
        #             if node.val in NodeDigits:
        #                 NodeDigits[node.val] += (0,1)
        #
        #     return NodeDigits
        #
        # NodeDigits = find(root, NodeDigits)
        # NodeDigits = find(root.left, NodeDigits)
        # NodeDigits = find(root.right, NodeDigits)
        # max_value = 0
        # for key, value in NodeDigits.items():
        #     (value1, value2)=value
        #     max_value = max(value2-value1+1, max_value)
        # return max_value-1

# root = TreeNode(5)
# root.left=TreeNode(4)
# root.right=TreeNode(5)
# root.left.left=TreeNode(1)
# root.left.right=TreeNode(1)
# root.right.right=TreeNode(5)

root = TreeNode(1)
root.left=TreeNode(4)
root.right=TreeNode(5)
root.left.left=TreeNode(4)
root.left.right=TreeNode(4)
root.right.right=TreeNode(5)
print(Solution().longestUnivaluePath(root))
