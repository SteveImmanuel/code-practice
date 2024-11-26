class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        node_dict = defaultdict(list)
        for x, y in edges:
            node_dict[y].append(x)
        
        champion = -1
        for i in range(n):
            if i not in node_dict:
                if champion == -1:
                    champion = i
                else:
                    return -1
            
        return champion