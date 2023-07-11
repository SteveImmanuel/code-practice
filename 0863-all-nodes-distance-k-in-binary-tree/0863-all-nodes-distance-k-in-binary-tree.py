# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Node:
    def __init__(self, x):
        self.val = x
        self.neighbors = []
    def __repr__(self):
        return 'val:' + str(self.val) + ' neighbor:' + str(self.neighbors)
    
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}
        self.tree_to_graph(root, graph)
        
        queue = deque([(target.val, 0)])
        visited = set()
        result = []
        while queue:
            cur_node, distance = queue.popleft()
            if distance > k or cur_node in visited:
                continue
            
            visited.add(cur_node)
            if distance == k:
                result.append(cur_node)
            else:
                for n in graph[cur_node].neighbors:
                    queue.append((n, distance + 1))
        
        return result
            
        
    def tree_to_graph(self, root, graph):
        if root.val not in graph:
            graph[root.val] = Node(root.val)
        
        if root.left:
            graph[root.val].neighbors.append(root.left.val)
            graph[root.left.val] = Node(root.left.val)
            graph[root.left.val].neighbors.append(root.val)
            self.tree_to_graph(root.left, graph)
        if root.right:
            graph[root.val].neighbors.append(root.right.val)
            graph[root.right.val] = Node(root.right.val)
            graph[root.right.val].neighbors.append(root.val)
            self.tree_to_graph(root.right, graph)