# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        result = []
        self.traverse(root, result)
        replace_dict = {}
        total = 0
        for i in range(len(result)-1,-1,-1):
            total += result[i]
            replace_dict[result[i]] = total
        self.replace(root, replace_dict)
        return root
    
    def traverse(self, root: TreeNode, result) -> TreeNode:
        if not root.left and not root.right:
            result.append(root.val)
        else:
            if root.left:
                self.traverse(root.left, result)
            result.append(root.val)
            if root.right:
                self.traverse(root.right, result)
    
    def replace(self, root, replace_dict):
        if root is None:
            return
        root.val = replace_dict[root.val]
        self.replace(root.left, replace_dict)
        self.replace(root.right, replace_dict)
        