# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.

# Solution without array exploitation
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        iterator = root
        prev_iterator = None
        found = False

        while not found:
            if iterator.left is not None:
                prev_iterator = iterator
                iterator = iterator.left
            else:
                found = True

        if k == 1:
            return iterator.val
        else:
            k -= 1
            if prev_iterator == None:
                return self.kthSmallest(root.right, k)
            else:
                if iterator.right is None:
                    if k == 1:
                        return prev_iterator.val
                    else:
                        total_right_child = self.get_total_nodes(prev_iterator.right)
                        if total_right_child >= k - 1:
                            return self.kthSmallest(prev_iterator.right, k - 1)
                        else:
                            k -= total_right_child
                            prev_iterator.left = None
                            prev_iterator.right = None
                            return self.kthSmallest(root, k)
                else:
                    total_right_child = self.get_total_nodes(iterator.right)
                    if total_right_child >= k:
                        return self.kthSmallest(iterator.right, k)
                    else:
                        k = k - total_right_child + 1
                        iterator.right = None
                        return self.kthSmallest(root, k)

    def get_total_nodes(self, root):
        if root is not None:
            return 1 + self.get_total_nodes(root.left) + self.get_total_nodes(root.right)
        return 0



sol = Solution()
# for i in range(1, 7):
#     root=TreeNode(5)
#     root.left = TreeNode(3)
#     root.right = TreeNode(6)
#     root.left.left = TreeNode(2)
#     root.left.right = TreeNode(4)
#     root.left.left.left = TreeNode(1)
#     print(sol.kthSmallest(root, i))

root=TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
print(sol.kthSmallest(root, 3))