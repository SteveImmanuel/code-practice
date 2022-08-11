# https://leetcode.com/problems/all-possible-full-binary-trees/
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2 == 0:
            return []

        if n == 1:
            return [TreeNode(0)]
        else:
            res = []
            for i in range(1, n, 2):
                # print(n, i)
                left_tree = self.allPossibleFBT(i)
                right_tree = self.allPossibleFBT(n - i - 1)

                for ltree in left_tree:
                    for rtree in right_tree:
                        root = TreeNode(0, ltree, rtree)
                        res.append(root)

            return res

sol = Solution()
tree = sol.allPossibleFBT(19)
print(len(tree))