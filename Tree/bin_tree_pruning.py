# https://leetcode.com/problems/binary-tree-pruning/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None and self.contain_one(root):
            self.prune_tree_rec(root)
            return root
        return None

    def prune_tree_rec(self, node):
        if node.left is not None:
            if node.left.val == 1 or self.contain_one(node.left):
                self.prune_tree_rec(node.left)
            else:
                node.left = None

        if node.right is not None:
            self.prune_tree_rec(node.right)
            if node.right.val == 1 or self.contain_one(node.right):
                self.prune_tree_rec(node.right)
            else:
                node.right = None
    
    def contain_one(self, node):
        if node.val == 1:
            return True
        else:
            left_contain = False
            right_contain = False
            if node.left is not None:
                left_contain = self.contain_one(node.left)
            if node.right is not None:
                right_contain = self.contain_one(node.right)
            return left_contain or right_contain

def print_tree_rec(root, res):
    if root is not None:
        res.append(root.val)
        if root.left is not None or root.right is not None:
            if root.left is not None:
                print_tree_rec(root.left, res)
            else:
                res.append(None)
            if root.right is not None:
                print_tree_rec(root.right, res)
            else:
                res.append(None)

root = TreeNode(0)
root.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(0)

res = []
print_tree_rec(root, res)
print(res)

sol = Solution()
root = sol.pruneTree(root)

res = []
print_tree_rec(root, res)
print(res)