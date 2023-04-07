class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        zeros_left = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    zeros_left.add((i, j))
                    
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([])
        
        if len(zeros_left) > 0:
            item = zeros_left.pop()
            zeros_left.add(item)
            queue = deque([item])
        
        valid = True
        current_land = 0
        total_land = 0
        while len(queue) > 0:
            i, j = queue.popleft()
            # print(i < 0, i >= m, j < 0, j >= n, (i, j) not in zeros_left, grid[i][j] != 0)
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) not in zeros_left or grid[i][j] != 1:
                if len(queue) == 0:
                    if valid:
                        total_land += current_land
                    
                    if len(zeros_left) > 0:
                        item = zeros_left.pop()
                        zeros_left.add(item)
                        queue.append(item)
                        valid = True
                        current_land = 0
                
                continue
                
            zeros_left.remove((i, j))
            current_land += 1
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                valid = False
                
            for delta in dirs:
                queue.append((i + delta[0], j + delta[1]))
            # print(queue)
            
        return total_land