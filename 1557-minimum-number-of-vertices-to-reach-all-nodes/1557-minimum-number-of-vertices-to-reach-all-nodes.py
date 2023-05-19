class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        node_connections = {}
        for start, end in edges:
            if start not in node_connections:
                node_connections[start] = []
            if end not in node_connections:
                node_connections[end] = []
            node_connections[end].append(start)
        
        res = []
        for key, value in node_connections.items():
            # print(key, value)
            if len(value) == 0:
                res.append(key)
        return res