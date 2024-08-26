"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.rec(root, res)
        return res
    
    def rec(self, root, res):
        if root is None:
            return
        if root.children is None:
            res.append(root.val)
            return
        
        for child in root.children:
            self.rec(child, res)
        res.append(root.val)
        