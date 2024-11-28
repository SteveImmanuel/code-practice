class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        heap = [(0, 0, 0)]
        
        visited = {(0, 0): 0}
        
        while len(heap) > 0:
            cost, i, j = heapq.heappop(heap)
                
            if (i, j) == (m-1, n-1):
                # break
                return cost
            
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ni = i + di
                nj = j + dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                
                ncost = cost + (1 if grid[ni][nj] == 1 else 0)
                if (ni, nj) in visited and visited[(ni, nj)] <= ncost:
                    continue
                    
                heapq.heappush(heap, (ncost, ni, nj))
                visited[(ni, nj)] = ncost