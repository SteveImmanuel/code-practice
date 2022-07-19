# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree_dict = self.get_nodes_each_level(root, 0)
        max_depth = max(tree_dict.keys())
        result = []
        
        for i in range(max_depth+1):
            if i%2 == 0 and tree_dict[i] != []:
                result.append(tree_dict[i])
            elif i%2 == 1 and tree_dict[i] != []:
                result.append(tree_dict[i][::-1])
        
        return result

    def get_nodes_each_level(self, root, current_depth):
        if root is None:
            return {current_depth: []}
        else:
            result = {current_depth: [root.val]}
            if root.left is not None:
                left_result = self.get_nodes_each_level(root.left, current_depth+1)
                result = self.combine_dict(result, left_result)

            if root.right is not None:
                right_result = self.get_nodes_each_level(root.right, current_depth+1)
                result = self.combine_dict(result, right_result)
            
            return result
    
    def combine_dict(self, ldict, rdict):
        result = {}
        for key in ldict.keys():
            if key in rdict:
                result[key] = ldict[key] + rdict[key]
            else:
                result[key] = ldict[key]
        
        for key in rdict.keys():
            if key not in result:
                result[key] = rdict[key]
        
        return result



root=TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(1)
# root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
# root = None
sol = Solution()
print(sol.zigzagLevelOrder(root))