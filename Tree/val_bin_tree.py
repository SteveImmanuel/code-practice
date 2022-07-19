from typing import Optional, List
# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTRec(root, None, None)

    def isValidBSTRec(self, root, lower_bound, upper_bound):
        if root == None:
            return True
        else:
            if lower_bound != None and root.val <= lower_bound:
                return False
            
            if upper_bound != None and root.val >= upper_bound:
                return False
            
            if lower_bound == None:
                new_lower_bound = root.val
            else:
                new_lower_bound = max(root.val, lower_bound)

            if upper_bound == None:
                new_upper_bound = root.val
            else:
                new_upper_bound = min(root.val, upper_bound)

            return self.isValidBSTRec(root.left, lower_bound, new_upper_bound) and self.isValidBSTRec(root.right, new_lower_bound, upper_bound)


sol = Solution()
tree = TreeNode(2, None, None)
tree.left = TreeNode(2, None, None)
tree.right = TreeNode(2, None, None)
# tree.right.left = TreeNode(3, None, None)
# tree.right.right = TreeNode(6, None, None)
# tree.left.left = TreeNode(1, None, None)
# tree.left.left.left = TreeNode(5, None, None)

# # tree = TreeNode(1, None, None)
# # tree.right = TreeNode(3, None, None)
# # tree.right.left = TreeNode(2, None, None)

# # tree = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
print(sol.isValidBST(tree))
# print(sol.tree_to_arr(tree))