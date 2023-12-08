# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        else:
            l_child = self.tree2str(root.left)
            r_child = self.tree2str(root.right)
            if r_child != '':
                r_child = '(' + r_child + ')'
                l_child = '(' + l_child + ')'
            elif l_child != '':
                l_child = '(' + l_child + ')'
            
            return str(root.val) + l_child + r_child