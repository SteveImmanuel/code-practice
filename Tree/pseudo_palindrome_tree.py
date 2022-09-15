# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
# Definition for a binary tree node.
from typing import Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        return self.pseudoPalindromicPathsRec(root, defaultdict(lambda:0))

    def pseudoPalindromicPathsRec(self, root, occ_dict):
        occ_dict[root.val] += 1
        if root.left is None and root.right is None:
            if self.is_pseudo_palindrome(occ_dict):
                return 1
            return 0
        else:
            total_left = 0
            total_right = 0
            if root.left is not None:
                total_left = self.pseudoPalindromicPathsRec(root.left, occ_dict.copy())
            if root.right is not None:
                total_right = self.pseudoPalindromicPathsRec(root.right, occ_dict.copy())
            return total_left + total_right
            # return self.pseudoPalindromicPathsRec(root.left, traversal_list.copy()) + self.pseudoPalindromicPathsRec(root.right, traversal_list.copy())

    def is_pseudo_palindrome(self, occ):
        chance = 1
        for val in occ.values():
            if val % 2 == 1:
                chance -= 1
        return chance >= 0

sol = Solution()
root = TreeNode(2)
root.right = TreeNode(1)
root.right.right = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)

# root = TreeNode(2)
# root.right = TreeNode(1)
# root.left = TreeNode(1)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.left.right.right = TreeNode(1)
print(sol.pseudoPalindromicPaths(root))