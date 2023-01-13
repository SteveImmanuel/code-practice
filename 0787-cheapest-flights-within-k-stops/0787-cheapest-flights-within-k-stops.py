class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost_dict = defaultdict(lambda: defaultdict(lambda: -1))
        edge_dict = defaultdict(list)
        for t_src, t_dst, price in flights:
            edge_dict[t_src].append((t_dst, price))

            
        for t_dst, price in edge_dict[src]:
            cost_dict[0][t_dst] = price
            
        for i in range(1, k+1):
            for current_node in cost_dict[i - 1]:
                current_price = cost_dict[i - 1][current_node]

                for next_node, price in edge_dict[current_node]:
                    total_price = current_price + price
                    if cost_dict[i][next_node] == -1:
                        cost_dict[i][next_node] = total_price
                    else:
                        cost_dict[i][next_node] = min(cost_dict[i][next_node], total_price)

                    if next_node in cost_dict[i - 1]:
                        cost_dict[i][next_node] = min(cost_dict[i][next_node], cost_dict[i-1][next_node])
            # print(i, cost_dict[i])
            # print()
        res = -1
        for i in range(k, -1, -1):
            if cost_dict[i][dst] != -1 and (res == -1 or cost_dict[i][dst] < res):
                res = cost_dict[i][dst]
            
        return res
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         neighbors = defaultdict(list)
        
#         for t_src, t_dst, price in flights:
#             neighbors[t_src].append((t_dst, price))
        
#         cheapest_price = self.dfs(src, dst, 0, set(), neighbors, k + 1)
#         return cheapest_price
        
#     def dfs(self, src, dst, cur_cost, visited, neighbors, remaining_hop):
#         if src == dst:
#             return cur_cost
#         elif remaining_hop == 0 and src != dst:
#             return -1
#         else:
#             visited.add(src)
#             len_visited = len(visited)
#             prices = []
            
#             for neighbor, cost in neighbors[src]:
#                 if neighbor not in visited:
#                     prices.append(self.dfs(neighbor, dst, cur_cost + cost, visited.copy(), neighbors, remaining_hop - 1))
            
#             min_price = None
#             for price in prices:
#                 if price != -1 and (min_price is None or price < min_price):
#                     min_price = price
            
#             if min_price is not None and min_price > 0:
#                 return min_price
#             return -1
        
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         neighbors = defaultdict(list)
        
#         for t_src, t_dst, price in flights:
#             neighbors[t_src].append((t_dst, price))
        
#         cheapest_price = self.dfs(src, dst, 0, [], neighbors, k + 1)
#         return cheapest_price
        
#     def dfs(self, src, dst, cur_cost, visited, neighbors, remaining_hop):
#         # print(src, dst, cur_cost, visited, remaining_hop)
#         if src == dst:
#             return cur_cost
#         elif remaining_hop == 0 and src != dst:
#             return -1
#         else:
#             visited.append(src)
#             len_visited = len(visited)
#             prices = []
            
#             for neighbor, cost in neighbors[src]:
#                 visited = visited[:len_visited]
#                 if neighbor not in visited:
#                     prices.append(self.dfs(neighbor, dst, cur_cost + cost, visited, neighbors, remaining_hop - 1))
            
#             min_price = None
#             for price in prices:
#                 if price != -1 and (min_price is None or price < min_price):
#                     min_price = price
            
#             if min_price is not None and min_price > 0:
#                 return min_price
#             return -1
            
            
            
            
