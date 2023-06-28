class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for edge, prob in zip(edges, succProb):
            graph[edge[0]].append((edge[1], prob))
            graph[edge[1]].append((edge[0], prob))

        heap = [(-1, start)]
        visited = set()
        while heap:
            cur_prob, cur_node = heappop(heap)
            if cur_node in visited:
                continue
            
            visited.add(cur_node)
            cur_prob *= -1
            if cur_node == end:
                return cur_prob
            
            for n, prob in graph[cur_node]:
                if n not in visited:
                    heappush(heap, (-1 * prob * cur_prob, n))
            # print(heap, visited)
        return 0
            
            
        
        
#     def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
#         graph = defaultdict(list)
#         for edge, prob in zip(edges, succProb):
#             graph[edge[0]].append((edge[1], prob))
#             graph[edge[1]].append((edge[0], prob))
        
#         visited = set()
#         mem = {}
#         prob = self.dfs(start, 1, end, graph, visited, mem) 
#         return prob
        
        
    # def dfs(self, cur_node, end, graph, visited, mem):
    #     # if cur_node not in mem:
    #     if cur_node == end:
    #         mem[cur_node] = cur_prob
    #     else:
    #         max_prob = 0
    #         for n, prob in graph[cur_node]:
    #             if n not in visited:
    #                 visited.add(n)
    #                 new_prob = self.dfs(n, cur_prob * prob, end, graph, visited, mem)
    #                 visited.discard(n)
    #                 max_prob = max(max_prob, new_prob)
    #         mem[cur_node] = max_prob
    #     return mem[cur_node]
                