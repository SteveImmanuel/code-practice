# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.min_depth_rec(1, root)
    
    def min_depth_rec(self, cur_depth, cur_node):
        if not cur_node.left and not cur_node.right:
            return cur_depth
        elif cur_node.left and not cur_node.right:
            return self.min_depth_rec(cur_depth + 1, cur_node.left)
        elif cur_node.right and not cur_node.left:
            return self.min_depth_rec(cur_depth + 1, cur_node.right)
        else:
            return min(self.min_depth_rec(cur_depth + 1, cur_node.left), self.min_depth_rec(cur_depth + 1, cur_node.right))