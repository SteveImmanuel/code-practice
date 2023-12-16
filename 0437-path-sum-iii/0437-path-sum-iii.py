# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.pathSumIter(root, targetSum)
        
    # def pathSumRec(self, root: Optional[TreeNode], targetSum: int, oriTarget) -> int:
    #     if not root:
    #         return 0
    #     print('visiting', root.val, 'target', targetSum)
    #     # if root.val > targetSum:
    #     #     return self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
    #     if root.val == targetSum:
    #         print(root.val)
    #         return 1
    #     else:
    #         l_include = self.pathSumRec(root.left, targetSum - root.val, oriTarget)
    #         r_include = self.pathSumRec(root.right, targetSum - root.val, oriTarget)
    #         l_exclude = self.pathSumRec(root.left, oriTarget, oriTarget)
    #         r_exclude = self.pathSumRec(root.right, oriTarget, oriTarget)
    #         print(root.val, l_include, r_include, l_exclude, r_exclude)
    #         return l_include + r_include + l_exclude + r_exclude - min(l_include, l_exclude) - min(r_include, r_exclude)
    
    def pathSumIter(self, root, targetSum):
        if not root:
            return 0
        else:
            # print(targetSum, root.val, self.pathSumRec(root, targetSum), self.pathSumIter(root.left, targetSum), self.pathSumIter(root.right, targetSum))
            return self.pathSumRec(root, targetSum) + self.pathSumIter(root.left, targetSum) + self.pathSumIter(root.right, targetSum)
    
    def pathSumRec(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        if root.val == targetSum:
            return 1 + self.pathSumRec(root.left, targetSum - root.val) + self.pathSumRec(root.right, targetSum - root.val)
        else:
            return self.pathSumRec(root.left, targetSum - root.val) + self.pathSumRec(root.right, targetSum - root.val)
    