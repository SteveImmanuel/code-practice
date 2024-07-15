# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_dict = {}
        child_set = set()
        for p, c, l in descriptions:
            if p not in node_dict:
                parent = TreeNode(p)
                node_dict[p] = parent
            if c not in node_dict:
                child = TreeNode(c)
                node_dict[c] = child
                
            parent = node_dict[p]
            child = node_dict[c]
            if l == 1:
                parent.left = child
            else:
                parent.right = child
            child_set.add(c)
        # print(child_set)
        for _, n in node_dict.items():
            if n.val not in child_set:
                return n
            
                