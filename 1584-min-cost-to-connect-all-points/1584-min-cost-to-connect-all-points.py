class Solution:
    def dist(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        vertices = [[99999999, i] for i in range(len(points))]
        vertices[0][0] = 0
        heapq.heapify(vertices)
        # print(vertices)
        # visited.add(0)
        total_cost = 0
        while len(visited) < len(points):
            cost, vertex = heapq.heappop(vertices)
            if vertex not in visited:
                visited.add(vertex)
                total_cost += cost
                
                for i in range(len(vertices)):
                    vertices[i][0] = min(self.dist(points[vertex], points[vertices[i][1]]), vertices[i][0])
                heapq.heapify(vertices)
            # print(len(visited))
        
        return total_cost
                
        