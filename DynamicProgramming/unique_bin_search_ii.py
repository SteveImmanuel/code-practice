# https://leetcode.com/problems/unique-binary-search-trees-ii/
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return 'root=' + str(self.val)

class Solution:
    def tree_to_arr(self, node) -> List:
        queue = []
        queue.append(node)
        res = []

        while len(queue) > 0:
            visited_node = queue.pop(0)
            # print('visitednode',visited_node)
            if visited_node == None:
                res.append(None)
            else:
                res.append(visited_node.val)
                queue.append(visited_node.left)
                queue.append(visited_node.right)
            # print('currentqueue',queue)
        
        while res[-1] == None:
            res.pop()

        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.genTreeRec(1, n)
    
    def genTreeRec(self, start_idx, end_idx):
        if start_idx > end_idx:
            return [None]

        total_nodes = end_idx - start_idx + 1
        result = []

        for i in range(start_idx, end_idx + 1):
            left_subtrees = self.genTreeRec(start_idx, i - 1)
            right_subtrees = self.genTreeRec(i + 1, end_idx)

            for lnode in left_subtrees:
                for rnode in right_subtrees:
                    root = TreeNode(i, lnode, rnode)
                    result.append(root)
        
        return result


sol = Solution()
n = 3


# # tree = TreeNode(3, None, None)
# # tree.left = TreeNode(2, None, None)
# # tree.left.left = TreeNode(1, None, None)

# # tree = TreeNode(1, None, None)
# # tree.right = TreeNode(3, None, None)
# # tree.right.left = TreeNode(2, None, None)

# # tree = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))

# print(sol.tree_to_arr(tree))
print(sol.generateTrees(n))