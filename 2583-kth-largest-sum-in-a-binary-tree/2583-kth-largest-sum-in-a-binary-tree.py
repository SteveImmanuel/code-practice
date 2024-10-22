# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_dict = defaultdict(int)
        self.rec(root, 0, level_dict)
        values = list(level_dict.values())
        values.sort(reverse=True)
        if k > len(values):
            return -1
        return values[k-1]

    
    def rec(self, root, level, level_dict):
        if not root:
            return
        
        level_dict[level] += root.val
        self.rec(root.left, level+1, level_dict)
        self.rec(root.right, level+1, level_dict)        