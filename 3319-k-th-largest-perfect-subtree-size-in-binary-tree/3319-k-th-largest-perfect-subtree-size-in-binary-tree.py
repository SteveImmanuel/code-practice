# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        results = []
        self.rec(root, results)
        if k - 1 >= len(results):
            return -1
        results.sort(reverse=True)
        # print(results)
        
        result = results[k - 1]
        return 2**result - 1
    
    def rec(self, cur, results):
        if cur is None:
            return 0
        
        if cur.left is None and cur.right is None:
            results.append(1)
            return 1
        
        left_best = self.rec(cur.left, results)
        right_best = self.rec(cur.right, results)
        if left_best == right_best and left_best != -1:
            results.append(left_best + 1)
            return left_best + 1
        else:
            return -1
        