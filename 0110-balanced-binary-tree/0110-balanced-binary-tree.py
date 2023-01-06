# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        elif not root.left and not root.right:
            return True
        else:
            ldepth = self.get_depth(root.left, 0)
            rdepth = self.get_depth(root.right, 0)
            return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(ldepth-rdepth) <= 1
    
    def get_depth(self, root, cur_depth):
        if not root:
            return cur_depth
        else:
            return max(self.get_depth(root.left, cur_depth+1), self.get_depth(root.right, cur_depth+1))