# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        
        root_val = postorder[-1]
        root = TreeNode(root_val)
        
        root_idx = inorder.index(root_val)
        linorder = inorder[:root_idx]
        rinorder = inorder[root_idx+1:]
        lpostorder = postorder[:len(linorder)]
        rpostorder = postorder[len(linorder):-1]
        
        root.left = self.buildTree(linorder, lpostorder)
        root.right = self.buildTree(rinorder, rpostorder)
        return root
        