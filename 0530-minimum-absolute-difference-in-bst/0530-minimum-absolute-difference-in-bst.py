# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []
        self.traverse(root, vals)
        vals.sort()
        min_diff = float('inf')
        for i in range(len(vals) - 1):
            min_diff = min(min_diff, abs(vals[i] - vals[i+1]))
        return min_diff
    
    def traverse(self, root, node_vals):
        if root:
            node_vals.append(root.val)
            self.traverse(root.left, node_vals)
            self.traverse(root.right, node_vals)            