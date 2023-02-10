class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cost_map = [[-1 for _ in range(n)] for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    
                    
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        # print(queue)
        while len(queue) > 0:
            cur_i, cur_j, cur_cost = queue.popleft()
            # print(cur_i < 0, cur_i >= n, cur_j < 0, cur_j >= n, cost_map[cur_i][cur_j] is not None, (grid[cur_i][cur_j] == 1 and cur_cost != 0))
            if cur_i < 0 or cur_i >= n or cur_j < 0 or cur_j >= n or cost_map[cur_i][cur_j] != -1 or (grid[cur_i][cur_j] == 1 and cur_cost != 0):
                continue
            cost_map[cur_i][cur_j] = cur_cost
            for dx, dy in dirs:
                queue.append((cur_i+dx, cur_j+dy, cur_cost+1))
        
        max_dist = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    max_dist = max(max_dist, cost_map[i][j])
        # for a in cost_map:
        #     print(a)
        return max_dist