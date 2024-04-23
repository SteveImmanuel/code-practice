class Solution:
    def get_farthest_node(self, start_node, graph):
        queue = deque([(start_node, 0)])
        visited = set([start_node])
        distance = {}
        while len(queue) > 0:
            cur_node, cur_cost = queue.popleft()
                
            found = False
            for neighbor in graph[cur_node]:
                if neighbor not in visited:
                    found = True
                    visited.add(neighbor)
                    queue.append((neighbor, cur_cost + 1))
            if not found:
                distance[cur_node] = cur_cost
        max_cost = max(distance.values())
        for key, val in distance.items():
            if val == max_cost:
                return key
    
    def find_path(self, cur_node, target_node, cur_path, visited, graph):
        cur_path.append(cur_node)
        visited.add(cur_node)
        
        if cur_node == target_node:
            return cur_path
        
        for neighbor in graph[cur_node]:
            if neighbor not in visited:
                path = self.find_path(neighbor, target_node, cur_path, visited, graph)
                if path is not None:
                    return path
        cur_path.pop()
        return None
        
        
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        for key in graph:
            if len(graph[key]) == 1:
                start_node = key
                break
        far_node1 = self.get_farthest_node(start_node, graph)
        far_node2 = self.get_farthest_node(far_node1, graph)
        
        path = self.find_path(far_node1, far_node2, [], set(), graph)
        
        if len(path) % 2 == 0:
            return [path[len(path) // 2], path[len(path) // 2 - 1]]
        else:
            return [path[len(path) // 2]]
            