# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, cur_level, level_mem):
        if not root:
            return
        
        level_mem[cur_level].append(root.val)
        self.traverse(root.left, cur_level+1, level_mem)
        self.traverse(root.right, cur_level+1, level_mem)
        
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_mem = defaultdict(list)
        self.traverse(root, 0, level_mem)
        res = []
        for item in level_mem.values():
            res.append(item[-1])
        return res
                