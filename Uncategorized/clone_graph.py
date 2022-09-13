# https://leetcode.com/problems/clone-graph/
"""
# Definition for a Node.
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        nodes_dict = {}
        self.create_nodes_dict(node, nodes_dict)
        visitation_dict = {key:False for key in nodes_dict.keys()}
        self.create_connection(node, nodes_dict, visitation_dict)
        return nodes_dict[node.val]


    def create_nodes_dict(self, node, nodes_dict):
        # node cannot be None
        nodes_dict[node.val] = Node(node.val)
        for neighbor in node.neighbors:
            if neighbor.val not in nodes_dict:
                self.create_nodes_dict(neighbor, nodes_dict)

    def create_connection(self, node, nodes_dict, visitation_dict):
        if visitation_dict[node.val]:
            return

        visitation_dict[node.val] = True
        for neighbor in node.neighbors:
            nodes_dict[node.val].neighbors.append(nodes_dict[neighbor.val])
            self.create_connection(neighbor, nodes_dict, visitation_dict)            
