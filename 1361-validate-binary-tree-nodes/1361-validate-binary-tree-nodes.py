class Node:
    def __init__(self, uid, left=None, right=None):
        self.uid = uid
        self.left = left
        self.right = right
        
    def __repr__(self):
        return str(self.uid)
    
class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        nodes = [Node(i) for i in range(n)]
        parent_none = set([i for i in range(n)])
        for i, (l, r) in enumerate(zip(leftChild, rightChild)):

            if leftChild[i] != -1:
                nodes[i].left = nodes[leftChild[i]]
            if rightChild[i] != -1:
                nodes[i].right = nodes[rightChild[i]]
            parent_none.discard(leftChild[i])
            parent_none.discard(rightChild[i])
        
        print(parent_none)
        if len(parent_none) != 1:
            return False
        
        checked = set()
        valid = self.traverse(nodes[parent_none.pop()], checked)
        return valid and len(checked) == n
        
    def traverse(self, cur_node, checked):
        if cur_node is None:
            return True
        
        if cur_node.uid in checked:
            return False
        
        checked.add(cur_node.uid)
        valid = True
        return self.traverse(cur_node.left, checked) and self.traverse(cur_node.right, checked)
        
                
        