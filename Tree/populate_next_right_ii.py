# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
from typing import Optional
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def calculate_depth(self, root):
        if root is not None:
            return 1 + max(self.calculate_depth(root.left), self.calculate_depth(root.right))
        return 0

    def get_nodes_of_level(self, root, current_level, target_level):
        if root is None:
            return []

        if current_level == target_level:
            return [root]
        else:
            left_nodes = self.get_nodes_of_level(root.left, current_level+1, target_level)
            right_nodes = self.get_nodes_of_level(root.right, current_level+1, target_level)
            return left_nodes + right_nodes

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        depth = self.calculate_depth(root)
        
        for i in range(1, depth + 1):
            leveled_nodes = self.get_nodes_of_level(root, 1, i)

            for j in range(len(leveled_nodes)):
                if j != len(leveled_nodes) - 1:
                    leveled_nodes[j].next = leveled_nodes[j+1]

        return root

root=Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.right.left = Node(6)
root.right.right = Node(7)
sol = Solution()
sol.connect(root)
for node in sol.get_nodes_of_level(root, 1, 3):
    print(node.val)
print(sol.get_nodes_of_level(root, 1, 3))