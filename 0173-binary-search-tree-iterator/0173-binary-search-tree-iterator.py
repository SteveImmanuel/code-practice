# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iterator = self.inorder_traversal(root)
        self.buffer = []

    def next(self) -> int:
        if len(self.buffer) > 0:
            return self.buffer.pop()
        return next(self.iterator)

    def hasNext(self) -> bool:
        if len(self.buffer) > 0:
            return True
        
        try:
            next_el = next(self.iterator)
            self.buffer.append(next_el)
            return True
        except:
            return False
        
        
    def inorder_traversal(self, root):
        if root is None:
            return
        yield from self.inorder_traversal(root.left)
        yield root.val
        yield from self.inorder_traversal(root.right)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()