# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level_dict = defaultdict(lambda: [None, None])
        self.traverse(root, [], level_dict)
        
        max_width = 0
        # print(level_dict)
        for start, end in level_dict.values():
            max_width = max(max_width, end - start + 1)
        return max_width
#         l_travel = []
#         r_travel = []
#         self.traverse(root, l_travel, True)
#         self.traverse(root, r_travel, False)
#         print(l_travel, r_travel)
        
#         cur_l = 0
#         cur_r = 0
#         max_width = 1
#         for i, (l, r) in enumerate(zip_longest(l_travel, r_travel)):
#             if l is None or r is None:
#                 max_width = max(max_width, 1)
#             else:
#                 cur_l *= 2
#                 if l == 'r':
#                     cur_l += 1
                    
#                 cur_r *= 2
#                 if r == 'r':
#                     cur_r += 1
                
#                 max_width = max(max_width, cur_r - cur_l + 1)
                    
                
#         return max_width
        
    def traverse(self, cur_node, traversal_list, level_dict):
        if not cur_node:
            return
        
        level = len(traversal_list)
        # print(cur_node.val, level, traversal_list)
        if level == 0:
            level_dict[level] = [0, 0]
        else:
            cur_value = int(''.join(traversal_list), 2)
            if level_dict[level][0] is None or cur_value < level_dict[level][0]:
                level_dict[level][0] = cur_value
            if level_dict[level][1] is None or cur_value > level_dict[level][1]:
                level_dict[level][1] = cur_value
        
        traversal_list.append('0')
        self.traverse(cur_node.left, traversal_list, level_dict)
        traversal_list.pop()
        traversal_list.append('1')
        self.traverse(cur_node.right, traversal_list, level_dict)
        traversal_list.pop()
        
        
#     def traverse(self, cur_node, travel_path, always_left):
#         if not cur_node:
#             return
        
#         if always_left:
#             if cur_node.left:
#                 travel_path.append('l')
#                 self.traverse(cur_node.left, travel_path, always_left)
#             elif cur_node.right:
#                 travel_path.append('r')
#                 self.traverse(cur_node.right, travel_path, always_left)
#         else:
#             if cur_node.right:
#                 travel_path.append('r')
#                 self.traverse(cur_node.right, travel_path, always_left)
#             elif cur_node.left:
#                 travel_path.append('l')
#                 self.traverse(cur_node.left, travel_path, always_left)
            
                
            