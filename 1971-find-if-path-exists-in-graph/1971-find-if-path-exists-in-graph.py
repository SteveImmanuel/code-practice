class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        path_dict = defaultdict(list)
        for node1, node2 in edges:
            path_dict[node1].append(node2)
            path_dict[node2].append(node1)
            
            
        visitation_map = [False] * n
        queue = deque([source])
        valid_dest = set()
        
        while len(queue) > 0:
            cur_node = queue.popleft()
            if visitation_map[cur_node]:
                continue
            
            visitation_map[cur_node] = True
            valid_dest.add(cur_node)
            for neighbor in path_dict[cur_node]:
                queue.append(neighbor)
        # print(valid_dest)
        return destination in valid_dest
        # return self.valid_path(source, destination, path_dict, visitation_map)
        
#     def valid_path(self, cur_node, target_node, path_dict, visitation_map):
#         if cur_node == target_node:
#             return True
        
#         visitation_map[cur_node] = True
#         for neighbor in path_dict[cur_node]:
#             if not visitation_map[neighbor] and self.valid_path(neighbor, target_node, path_dict, visitation_map.copy()):
#                 return True
#         return False