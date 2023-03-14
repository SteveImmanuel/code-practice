# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result_list = []
        self.traverse(root, [], result_list)
        # print(result_list)
        return sum(result_list)
    
    def traverse(self, root, iteration_list, result_list):
        iteration_list.append(root.val)
        if not root.left and not root.right:
            total = 0
            for num in iteration_list:
                total = total * 10 + num
            result_list.append(total)
        else:
            len_iteration_list = len(iteration_list)
            if root.left:
                iteration_list = iteration_list[:len_iteration_list]
                self.traverse(root.left, iteration_list, result_list)
            if root.right:
                iteration_list = iteration_list[:len_iteration_list]
                self.traverse(root.right, iteration_list, result_list)
            