class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = {}
        for start, end in edges:
            if start not in root:
                root[start] = start
            if end not in root:
                root[end] = end
                
            if self.is_connected(start, end, root):
                return [start, end]
            
            self.union(start, end, root)
    
    def get_root(self, x, root):
        while x != root[x]:
            x = root[x]
        return x
    
    def union(self, x, y, root):
        rootx = self.get_root(x, root)
        rooty = self.get_root(y, root)
        if rootx != rooty:
            root[rooty] = rootx
    
    def is_connected(self, x, y, root):
        return self.get_root(x, root) == self.get_root(y, root)