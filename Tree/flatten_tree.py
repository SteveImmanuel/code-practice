# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        deepest_left = None
        if root.left is not None:
            left = self.flatten(root.left)

            deepest_left = root.left
            while deepest_left.right is not None:
                deepest_left = deepest_left.right

            root.left = None

        if root.right is not None:
            right = self.flatten(root.right)
            if deepest_left is not None:
                root.right = left
                deepest_left.right = right
        else:
            if deepest_left is not None:
                root.right = left

        return root

        
tree = TreeNode(1, None, None)
tree.left = TreeNode(2, None, None)
# tree.right = TreeNode(5, None, None)
# tree.right.left = TreeNode(9, None, None)
# tree.right.right = TreeNode(6, None, None)
# tree.left.left = TreeNode(3, None, None)
# tree.left.right = TreeNode(4, None, None)

sol = Solution()
sol.flatten(tree)

while tree is not None:
    print(tree.val)
    tree = tree.right