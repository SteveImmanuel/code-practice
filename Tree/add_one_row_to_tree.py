# https://leetcode.com/problems/add-one-row-to-tree/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right\

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        return self.add_rec(root, val, 1, depth)
        
    def add_rec(self, root, val, current_depth, depth):
        if depth == 1:
            node = TreeNode(val, root)
            return node
        
        if current_depth == depth - 1:
            left_node = TreeNode(val, root.left, None)
            right_node = TreeNode(val, None, root.right)
            root.left = left_node
            root.right = right_node
        else:
            if root.left:
                self.add_rec(root.left, val, current_depth+1, depth)
            if root.right:
                self.add_rec(root.right, val, current_depth+1, depth)
            
        return root
                

sol = Solution()
root=TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)
val = 1
depth = 2
sol.addOneRow(root, val, depth)
print(root.left.val, root.left.right, root.right.val, root.right.left)