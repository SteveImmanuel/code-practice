# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        roots = []
        self.traverse_down(root)
        self.del_rec(root, roots, to_delete, True)
        return roots
    
    def traverse_down(self, root):
        if not root:
            return
        
        if root.left is not None:
            root.left.parent = (root, 'l')
            self.traverse_down(root.left)
        
        if root.right is not None:
            root.right.parent = (root, 'r')
            self.traverse_down(root.right)
    
    def del_rec(self, cur, roots, to_delete, parent_deleted):
        if cur is None:
            return
        # print(cur.val, cur.val in to_delete)
        if cur.val in to_delete:
            if hasattr(cur, 'parent'):
                parent, child_dir = cur.parent
                # print(parent.val, child_dir)
                if child_dir == 'l':
                    parent.left = None
                else:
                    parent.right = None
            deleted = True
        else:
            if parent_deleted:
                roots.append(cur)
            deleted = False
        
        self.del_rec(cur.left, roots, to_delete, deleted)
        self.del_rec(cur.right, roots, to_delete, deleted)
            
            
        

