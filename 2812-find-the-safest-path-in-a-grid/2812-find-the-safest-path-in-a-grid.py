class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        thief_idx = []
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    thief_idx.append((i, j))
        
        deltas = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        cost_mat = [[float('inf') for _ in range(n)] for _ in range(n)]
        queue = deque([(i, j, 0) for i, j in thief_idx])
        while queue:
            ci, cj, cost = queue.popleft()
            
            if cost_mat[ci][cj] is None or cost < cost_mat[ci][cj]:
                cost_mat[ci][cj] = cost
            
                for delta in deltas:
                    if ci + delta[0] < 0 or ci + delta[0] >= n or cj + delta[1] < 0 or cj + delta[1] >= n:
                        continue
                    else:
                        if cost_mat[ci + delta[0]][cj + delta[1]] is not None and cost_mat[ci + delta[0]][cj + delta[1]] <= cost + 1:
                            continue
                        queue.append((ci + delta[0], cj + delta[1], cost + 1))
        
        heap = [(-cost_mat[0][0], 0, 0)]
        safe_mat = [[None for _ in range(n)] for _ in range(n)]
        
        while heap:
            safeness, ci, cj = heapq.heappop(heap)
            safeness *= -1

            if safe_mat[ci][cj] is None or safeness > safe_mat[ci][cj]:
                safe_mat[ci][cj] = safeness

                for delta in deltas:
                    if 0 <= ci + delta[0] < n and 0 <= cj + delta[1] < n:
                        n_safeness = min(safeness, cost_mat[ci + delta[0]][cj + delta[1]])
                        if safe_mat[ci + delta[0]][cj + delta[1]] is not None and safe_mat[ci + delta[0]][cj + delta[1]] >= n_safeness:
                            continue
                        heapq.heappush(heap, (-n_safeness, ci + delta[0], cj + delta[1]))

        return safe_mat[-1][-1]
                
                