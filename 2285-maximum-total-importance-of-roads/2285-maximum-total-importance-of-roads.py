class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(int)
        for a, b in roads:
            graph[a] += 1
            graph[b] += 1
        sorted_cities = list(graph.items())
        sorted_cities.sort(key=lambda x: x[1], reverse=True)
        # print(sorted_cities)
        val = n
        importance = [None] * n
        for city, _ in sorted_cities:
            importance[city] = val
            val -= 1
        # print(importance)
        total = 0
        for a, b in roads:
            total += importance[a] + importance[b]
        return total