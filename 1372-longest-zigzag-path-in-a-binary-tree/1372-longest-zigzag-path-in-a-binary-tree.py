# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = self.get_longest(root)
        # print(res)
        return res[-1]
    
    def get_longest(self, cur_node):
        # print(cur_node.val, not cur_node.left, not cur_node.right)
        if not cur_node.left and not cur_node.right:
            return (0, 0, 0)
        
        # left case
        l = 0
        cur_max = 0
        if cur_node.left:
            _, r_max, r_all_max = self.get_longest(cur_node.left)
            # print('l', _, r_max)
            cur_max = max(cur_max, r_all_max)
            l = r_max + 1
            
        # right case
        r = 0
        if cur_node.right:
            l_max, _, l_all_max = self.get_longest(cur_node.right)
            # print('r', l_max, _)
            cur_max = max(cur_max, l_all_max)
            r = l_max + 1
        
        return (l, r, max(l, r, cur_max))