# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        level_dict = defaultdict(list)
        self.serialize_tree(root, 0, level_dict)
        result = []
        key = 0
        while key in level_dict:
            result += level_dict[key]
            key += 1
        # print(result)
        
        has_seen_none = False
        for num in result:
            if num is None:
                has_seen_none = True
            else:
                if has_seen_none:
                    return False
        return True
    
    def serialize_tree(self, root, cur_level, level_dict):
        if root:
            level_dict[cur_level].append(root.val)
            self.serialize_tree(root.left, cur_level+1, level_dict)
            self.serialize_tree(root.right, cur_level+1, level_dict)            
        else:
            level_dict[cur_level].append(root)