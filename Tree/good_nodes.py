# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesRec(root, [])

    def goodNodesRec(self, root, traversal_list):
        self_good_node = 0
        if len(traversal_list) == 0:
            self_good_node = 1
        else:
            max_val = max(traversal_list)
            if max_val <= root.val:
                self_good_node = 1

        new_traversal_list = [*traversal_list, root.val]
        left_good_node = 0
        right_good_node = 0
        if root.left is not None:
            left_good_node = self.goodNodesRec(root.left, new_traversal_list)
        if root.right is not None:
            right_good_node = self.goodNodesRec(root.right, new_traversal_list)
        
        return self_good_node + right_good_node + left_good_node

sol = Solution()
# tree = TreeNode(3)
# tree.left = TreeNode(1)
# tree.right = TreeNode(4)
# tree.left.left = TreeNode(3)
# tree.right.left = TreeNode(1)
# tree.right.right = TreeNode(5)


tree = TreeNode(3)
tree.left = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(2)
print(sol.goodNodes(tree))