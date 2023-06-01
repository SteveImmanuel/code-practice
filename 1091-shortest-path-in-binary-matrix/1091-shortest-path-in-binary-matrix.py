class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([(0, 0, 1)])
        n = len(grid)
        visited = set()
        
        deltas = [(0, -1), (-1, 0), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        while queue:
            i, j, cost = queue.popleft()
            if i < 0 or i >= n or j < 0 or j >= n or (i, j) in visited or grid[i][j] != 0:
                continue
                
            visited.add((i, j))
            if i == n - 1 and j == n - 1:
                return cost
            else:
                for delta in deltas:
                    queue.append((i + delta[0], j + delta[1], cost + 1))
        return -1
                