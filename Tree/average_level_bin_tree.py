# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Definition for a binary tree node.
from typing import Optional, List
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        lev_dict = defaultdict(lambda:[])
        self.get_level_rec(root, 0, lev_dict)
        res = []
        for key in lev_dict:
            res.append(sum(lev_dict[key])/len(lev_dict[key]))
        return res

    def get_level_rec(self, root, cur_lev, lev_dict):
        if root is not None:
            lev_dict[cur_lev].append(root.val)
            self.get_level_rec(root.left, cur_lev+1, lev_dict)
            self.get_level_rec(root.right, cur_lev+1, lev_dict)

sol = Solution()
tree = TreeNode(3, None, None)
tree.left = TreeNode(9, None, None)
tree.right = TreeNode(20, None, None)
tree.right.left = TreeNode(15, None, None)
tree.right.right = TreeNode(7, None, None)

print(sol.averageOfLevels(tree))