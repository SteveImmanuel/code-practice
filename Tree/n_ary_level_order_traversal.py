# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
from typing import List
from collections import defaultdict
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = defaultdict(lambda: [])
        self.level_order_rec(root, 0, res)
        return list(res.values())

    def level_order_rec(self, root, current_level, res):
        if root is None:
            return
        
        res[current_level].append(root.val)
        if root.children is not None:
            for child in root.children:
                self.level_order_rec(child, current_level+1, res)

sol = Solution()
root = Node(1)
root.children = [Node(3), Node(2), Node(4)]
root.children[0].children = [Node(5), Node(6)]
print(sol.levelOrder(root))