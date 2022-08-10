# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid+1:]
        return TreeNode(nums[mid], self.sortedArrayToBST(left), self.sortedArrayToBST(right))

sol = Solution()
nums = [-10,-3,0,5,9]
tree = sol.sortedArrayToBST(nums)