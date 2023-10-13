class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for s, e in paths:
            graph[s-1].append(e-1)
            graph[e-1].append(s-1)            
            
        result = [None] * n
        visited = set()
        for i in range(n):
            # print(visited)
            if i not in visited:
                visited.add(i)
                self.dfs(i, graph, result, visited)
                # print(i, result, visited)
        return result
        
    def dfs(self, cur_g, graph, result, visited):
        possible_color = set([i for i in range(1, 5)])
        for neighbor in graph[cur_g]:
            if result[neighbor] is not None:
                possible_color.discard(result[neighbor])
        
        enter_neighbor = False
        for f in possible_color:
            result[cur_g] = f
                        
            for neighbor in graph[cur_g]:
                if neighbor not in visited:
                    enter_neighbor = True
                    visited.add(neighbor)
                    valid = self.dfs(neighbor, graph, result, visited)
                    if not valid:
                        visited.remove(neighbor)
                    else:
                        return True
        
        if enter_neighbor:
            return False
        
        return len(possible_color) > 0
