class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # graph = defaultdict(list)
        # for a, b in edges:
        #     graph[a].append(b)
        #     graph[b].append(a)
        # for key in graph:
        #     if len(graph[key]) == len(graph) - 1:
        #         return key
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]