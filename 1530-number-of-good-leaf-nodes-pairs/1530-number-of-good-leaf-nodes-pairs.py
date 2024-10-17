# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        all_leaves = []
        self.traverse_down(root, all_leaves)
        
        leaf_parents = []
        for leaf in all_leaves:
            parent = []
            cur_node = leaf
            k = 1
            while k < distance:
                if not hasattr(cur_node, 'parent'):
                    break
                cur_node = cur_node.parent
                parent.append(cur_node)
                k += 1
            leaf_parents.append(parent)
        
        total = 0
        for i in range(len(leaf_parents)):
            for j in range(i+1, len(leaf_parents)):
                found = False
                for k in range(len(leaf_parents[i])):
                    for l in range(len(leaf_parents[j])):
                        if leaf_parents[i][k] == leaf_parents[j][l] and k + l + 2 <= distance:
                            found = True
                            break
                    if found:
                        break
                
                if found:
                    total += 1
        
        return total

    def traverse_down(self, root, all_leaves):
        if not root:
            return
        
        if root.left is not None:
            root.left.parent = root
            self.traverse_down(root.left, all_leaves)
        
        if root.right is not None:
            root.right.parent = root
            self.traverse_down(root.right, all_leaves)
        
        if root.left is None and root.right is None:
            all_leaves.append(root)
    

        
        
            