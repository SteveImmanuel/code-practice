# https://leetcode.com/problems/path-sum-ii/
# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result_list = []
        traversal_list = []
        self.path_sum_rec(root, targetSum, traversal_list, 0, result_list)
        return result_list

    def path_sum_rec(self, root, target, traversal_list, current_sum, result_list):
        if root:
            if not root.left and not root.right:
                if current_sum + root.val == target:
                    result_list.append(traversal_list + [root.val])
            else:
                traversal_list.append(root.val)
                len_travelsal_list = len(traversal_list)
                if root.left:
                    self.path_sum_rec(root.left, target, traversal_list, current_sum+root.val, result_list)
                traversal_list = traversal_list[:len_travelsal_list]
                if root.right:
                    self.path_sum_rec(root.right, target, traversal_list, current_sum+root.val, result_list)
                traversal_list = traversal_list[:len_travelsal_list]
                



root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

sol = Solution()
print(sol.pathSum(root, 22))