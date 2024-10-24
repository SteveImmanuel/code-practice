# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        
        if (root1 is None and root2 is not None) or (root2 is None and root1 is not None) or root1.val != root2.val:
            return False
        
        if (root1.left is None and root2.left is not None) or (root1.left is not None and root2.left is None) or (root1.left is not None and root2.left is not None and root1.left.val != root2.left.val):
            temp = root1.left
            root1.left = root1.right
            root1.right = temp
            
        left_same = self.flipEquiv(root1.left, root2.left)
        right_same = self.flipEquiv(root1.right, root2.right)
        
        return left_same and right_same