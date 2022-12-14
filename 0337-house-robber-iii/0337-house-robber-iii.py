# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.traverse(root)
        # print(res)
        return max(res)
    
    def traverse(self, root):
        if not root:
            return (0,0)
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        return (root.val + left[1] + right[1], max(left) + max(right))