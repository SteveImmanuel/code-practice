# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, level, res):
        if not root:
            return
        
        res[level].append(root.val)
        self.traverse(root.left, level + 1, res)
        self.traverse(root.right, level + 1, res)
    
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = defaultdict(list)
        self.traverse(root, 1, res)
        
        cur_max = -float('inf')
        cur_max_idx = -1
        i = 1
        while i in res:
            cur_sum = sum(res[i])
            if cur_sum > cur_max:
                cur_max = cur_sum
                cur_max_idx = i
            i += 1
        return cur_max_idx
        
        