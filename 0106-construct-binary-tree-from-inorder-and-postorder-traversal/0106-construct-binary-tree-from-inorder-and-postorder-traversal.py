# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         if len(inorder) == 0:
#             return None
        
#         root_val = postorder[-1]
#         root = TreeNode(root_val)
        
#         root_idx = inorder.index(root_val)
#         linorder = inorder[:root_idx]
#         rinorder = inorder[root_idx+1:]
#         lpostorder = postorder[:len(linorder)]
#         rpostorder = postorder[len(linorder):-1]
        
#         root.left = self.buildTree(linorder, lpostorder)
#         root.right = self.buildTree(rinorder, rpostorder)
#         return root
        return self.buildTreeRec(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)
    
    def buildTreeRec(self, inorder, postorder, l_in, r_in, l_post, r_post):
        if l_in > r_in:
            return None
        
        root_val = postorder[r_post]
        root = TreeNode(root_val)
        root_idx = inorder.index(root_val)
        
        left_l_in = l_in
        left_r_in = root_idx - 1
        right_l_in = root_idx + 1
        right_r_in = r_in
        
        left_l_post = l_post
        left_r_post = l_post + (left_r_in - left_l_in)
        right_l_post = l_post + (left_r_in - left_l_in) + 1
        right_r_post = r_post - 1
        
        root.left = self.buildTreeRec(inorder, postorder, left_l_in, left_r_in, left_l_post, left_r_post)
        root.right = self.buildTreeRec(inorder, postorder, right_l_in, right_r_in, right_l_post, right_r_post)
        return root
        