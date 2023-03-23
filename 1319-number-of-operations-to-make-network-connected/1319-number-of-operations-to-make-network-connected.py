class QuickFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1
                
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        spare_cables = 0
        
        graph = QuickFind(n)
        for c1, c2 in connections:
            if graph.is_connected(c1, c2):
                spare_cables += 1
            else:
                graph.union(c1, c2)
                
        # print(spare_cables, graph.root)
        for i in range(n):
            graph.find(i)
        
        total_disjoint = len(set(graph.root))
        
        if total_disjoint - 1 <= spare_cables:
            return total_disjoint - 1
        return -1
        