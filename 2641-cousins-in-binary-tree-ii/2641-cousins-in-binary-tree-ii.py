# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = defaultdict(int)
        self.levelrec(root, 0, level_sum)
        # print(level_sum)
        self.traverse(root, 0, level_sum, 0)
        return root
        
    def levelrec(self, root, level, level_sum):
        if not root:
            return
        
        level_sum[level] += root.val
        self.levelrec(root.left, level+1, level_sum)
        self.levelrec(root.right, level+1, level_sum)        
        
    def traverse(self, root, level, level_sum, replaceval):
        if not root:
            return
        
        root.val = replaceval
        next_replaceval = level_sum[level+1]
        if root.left:
            next_replaceval -= root.left.val
        if root.right:
            next_replaceval -= root.right.val
        self.traverse(root.left, level+1, level_sum, next_replaceval)
        self.traverse(root.right, level+1, level_sum, next_replaceval)
        
            
        
        
        