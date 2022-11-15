# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # res = self.count(root, 0, [])
        # print(res)
        return self.count2(root)
        
        
    def get_depth(self, current_depth, root, traversal_list):
        if not root.left and not root.right: # leaf
            return
        
        if not root.left or not root.right:
            return traversal_list
        
        len_traversal_list = len(traversal_list)
        traversal_list.append('r')
        temp = self.get_depth(current_depth+1, root.right, traversal_list)
        if temp:
            return temp
        traversal_list = traversal_list[:len_traversal_list]
        traversal_list.append('l')
        temp = self.get_depth(current_depth+1, root.left, traversal_list)
        traversal_list = traversal_list[:len_traversal_list]
        return temp

    def count(self, root, current_depth, traversal_list):
        if not root:
            return -1
        
        print(root.val)
        
        if not root.left and not root.right: # leaf
            return current_depth
        
        len_traversal_list = len(traversal_list)

        traversal_list.append('r')
        r_count = self.count(root.right, current_depth+1, traversal_list)
        traversal_list = traversal_list[:len_traversal_list]
        if type(r_count) == tuple:
            return r_count
        
        
        traversal_list.append('l')
        l_count = self.count(root.left, current_depth+1, traversal_list)
        traversal_list = traversal_list[:len_traversal_list]
        if type(l_count) == tuple:
            return l_count
        
        if r_count == l_count:
            return max(r_count, l_count)
        else:
            return (l_count, traversal_list)
        
    def count2(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right: # leaf
            return 1
        
        return 1 + self.count2(root.left) + self.count2(root.right)            
        
