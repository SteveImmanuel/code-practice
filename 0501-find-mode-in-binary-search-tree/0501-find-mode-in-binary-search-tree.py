# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        mem = defaultdict(int)
        self.traverse(root, mem)
        nodes = list(mem.items())
        nodes.sort(key=lambda x:x[1])
        max_occ = nodes[-1][-1]
        res = []
        for i in range(len(nodes) - 1, -1, -1):
            if nodes[i][1] == max_occ:
                res.append(nodes[i][0])
            else:
                break
        return res
    
    def traverse(self, root, mem):
        if not root:
            return
        
        mem[root.val] += 1
        self.traverse(root.left, mem)
        self.traverse(root.right, mem)        