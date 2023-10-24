# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        level_dict = defaultdict(list)
        self.traverse(root, 0, level_dict)
        res = list(map(max, level_dict.values()))
        return res
    
    def traverse(self, cur_node, cur_depth, level_dict):
        if not cur_node:
            return
        
        level_dict[cur_depth].append(cur_node.val)
        self.traverse(cur_node.left, cur_depth + 1, level_dict)
        self.traverse(cur_node.right, cur_depth + 1, level_dict)        