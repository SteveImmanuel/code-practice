# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_list = []
        _, _, _, _, _, res = self.traverse(root, -100000000)
        return res
        
    def traverse(self, root, cur_max):
        if not root:
            return 0, 0, 0, False, False, -100000000
        
        l_res = self.traverse(root.left, cur_max)
        r_res = self.traverse(root.right, cur_max)
        
        cur_max = max(cur_max, l_res[-1], r_res[-1])
        
        #calculate l_max
        if l_res[3] and l_res[4]:
            if l_res[1] > l_res[2]:
                l_max = l_res[0] - l_res[2]
            else:
                l_max = l_res[0] - l_res[1]
        else:
            l_max = l_res[0]
        
        #calculate r_max
        if r_res[3] and r_res[4]:
            if r_res[1] > r_res[2]:
                r_max = r_res[0] - r_res[2]
            else:
                r_max = r_res[0] - r_res[1]
        else:
            r_max = r_res[0]
        
        
        if l_max <= 0 and r_max <= 0:
            return root.val, 0, 0, False, False, max(cur_max, root.val)
        elif l_max <= 0:
            return root.val + r_max, 0, r_max, False, True, max(cur_max, root.val + r_max)
        elif r_max <= 0:
            return root.val + l_max, l_max, 0, True, False, max(cur_max, root.val + l_max)
        else:
            return root.val + l_max + r_max, l_max, r_max, True, True, max(cur_max, root.val + l_max + r_max)
        
        