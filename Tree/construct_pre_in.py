# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 and len(inorder) == 0:
            return None
            
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        left_in = inorder[:root_idx]
        right_in = inorder[root_idx+1:]
        left_pre = preorder[1:1+len(left_in)]
        right_pre = preorder[1+len(left_in):]

        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)
        return root

sol = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
tree = sol.buildTree(preorder, inorder)