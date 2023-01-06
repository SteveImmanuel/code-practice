# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        longest_l = self.diameterOfBinaryTree(root.left)
        longest_r = self.diameterOfBinaryTree(root.right)
        return max(longest_l, longest_r, self.get_depth(root.left, 1) + self.get_depth(root.right, 1))
    
    def get_depth(self, root, cur_depth):
        if not root:
            return cur_depth - 1
        else:
            return max(self.get_depth(root.left, cur_depth+1), self.get_depth(root.right, cur_depth+1))