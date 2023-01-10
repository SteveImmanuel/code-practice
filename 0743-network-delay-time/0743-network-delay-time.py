class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cost_dict = defaultdict(list)
        for start, end, cost in times:
            cost_dict[start].append((cost, end))
            
        visited = set()
        queue = [(0, k)]
        current_timestamp = 0
        
        while len(queue) > 0:
            # print(queue)
            cost, node = heapq.heappop(queue)
            if node not in visited:
                visited.add(node)
                current_timestamp = max(current_timestamp, cost)
                
                for cost, neighbor in cost_dict[node]:
                    heapq.heappush(queue, (cost + current_timestamp, neighbor))
        
        if len(visited) == n:
            return current_timestamp
        
        return -1
        
        
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         MAX_CONST = 99999
#         cost_matrix = [[MAX_CONST for _ in range(n)] for _ in range(n)]
#         for start, end, time in times:
#             cost_matrix[start - 1][end - 1] = time
        
#         visited = set()
#         vertices = [[MAX_CONST, i + 1] for i in range(n)]
#         vertices[k - 1][0] = 0
#         heapq.heapify(vertices)
#         # print(vertices)
#         # visited.add(0)

#         total_cost = 0
#         while len(visited) < n:
#             print(vertices)
#             cost, vertex = heapq.heappop(vertices)
#             if vertex not in visited:
#                 if cost < MAX_CONST:
#                     visited.add(vertex)
#                     total_cost += cost

#                     for i in range(len(vertices)):
#                         vertices[i][0] = min(cost_matrix[vertex - 1][vertices[i][1] - 1], vertices[i][0])
#                     heapq.heapify(vertices)
#                 else:
#                     return -1
#             # print(len(visited))
        
#         return total_cost
                