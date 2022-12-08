# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = []
        leaves2 = []
        self.get_leaves(root1, leaves1)
        self.get_leaves(root2, leaves2)
        return leaves1 == leaves2
        
        
    def get_leaves(self, root, leaves):
        if not root:
            return
        
        if not root.left and not root.right:
            leaves.append(root.val)
        else:
            self.get_leaves(root.left, leaves)
            self.get_leaves(root.right, leaves)
            