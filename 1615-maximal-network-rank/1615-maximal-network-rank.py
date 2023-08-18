class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
            
        cities = [(k, v, len(v)) for (k, v) in list(graph.items())]
        # cities.sort(key= lambda x:x[-1], reverse=True)
        # print(cities)
        max_rank = 0
        for i in range(len(cities)):
            for j in range(i+1, len(cities)):
                # print(i, j)
                max_rank = max(max_rank, cities[i][-1] + cities[j][-1] - (1 if cities[i][0] in cities[j][1] else 0))
        
        return max_rank
#         print(cities)
        
#         if len(cities) == 0:
#             return 0
        
#         max_rank = 0
#         for i in range(1, len(cities)):
#             max_rank = max(max_rank, cities[i][-1] - (1 if cities[0][0] in cities[i][1] else 0))
        
#         return max_rank + cities[0][-1]
            