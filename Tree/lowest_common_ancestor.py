# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_node(self, root, target, traversal_list):
        if root.val != target.val:
            new_traversal_list = traversal_list.copy()
            new_traversal_list.append(root)
            
            res = []
            if root.left is None and root.right is None:
                return []
            elif root.left is not None:
                res = self.find_node(root.left, target, new_traversal_list)
            
            if root.right is not None and res == []:
                res = self.find_node(root.right, target, new_traversal_list)
            
            return res
        else:
            traversal_list.append(root)
            return traversal_list


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_traversal_list = self.find_node(root, p, [])
        q_traversal_list = self.find_node(root, q, [])
        q_traversal_list = set(q_traversal_list)
        common_ancestor = [el for el in p_traversal_list if el in q_traversal_list]
        return common_ancestor[-1]



sol = Solution()
tree = TreeNode(3)
tree.left = TreeNode(5)
tree.right = TreeNode(1)
tree.left.left = TreeNode(6)
tree.left.right = TreeNode(2)
tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(4)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(8)

# print(sol.lowestCommonAncestor(tree, tree.left, tree.right).val)
print(sol.lowestCommonAncestor(tree, tree.left, tree.left.right.right).val)
# print(sol.lowestCommonAncestor(tree, tree.left, tree.left.right.right).val)
# temp = sol.find_node(tree, tree.left.right.right, [])
# for a in temp:
#     print(a.val)