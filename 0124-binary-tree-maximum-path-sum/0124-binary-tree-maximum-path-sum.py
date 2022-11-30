# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_list = []
        self.traverse(root, max_path_list)
        return max(max_path_list)
        
    def traverse(self, root, max_path_list):
        if not root:
            return 0, 0, 0, False, False
        
        l_res = self.traverse(root.left, max_path_list)
        r_res = self.traverse(root.right, max_path_list)
        
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
            max_path_list.append(root.val)
            return root.val, 0, 0, False, False
        elif l_max <= 0:
            max_path_list.append(root.val + r_max)
            return root.val + r_max, 0, r_max, False, True
        elif r_max <= 0:
            max_path_list.append(root.val + l_max)
            return root.val + l_max, l_max, 0, True, False
        else:
            max_path_list.append(root.val + l_max + r_max)
            return root.val + l_max + r_max, l_max, r_max, True, True
        
        