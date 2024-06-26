# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.traverse(root, arr)
        return self.build_tree(arr, 0, len(arr) - 1)
        
    def build_tree(self, arr, left, right):
        if left == right:
            return TreeNode(arr[left])
        elif left > right:
            return None
        else:
            mid = (left + right) // 2
            root = TreeNode(arr[mid])
            root.left = self.build_tree(arr, left, mid - 1)
            root.right = self.build_tree(arr, mid + 1, right)
            return root
        
        
    def traverse(self, root, result):
        if not root:
            return
        else:
            self.traverse(root.left, result)
            result.append(root.val)
            self.traverse(root.right, result)