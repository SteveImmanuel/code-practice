class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        queue = deque()
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        total_step = 0
        visited = set()
        # print('start')
        queue.append((entrance[0], entrance[1], total_step))
        while len(queue) > 0:
            i, j, total_step = queue.popleft()
            if i < 0 or i >= m or j < 0 or j >= n or (i,j) in visited or maze[i][j] == '+':
                continue
            # print(i,j,total_step)
            visited.add((i,j))
            if (i == 0 or j == 0 or i == m-1 or j == n-1) and not (i == entrance[0] and j == entrance[1]):
                return total_step
            
            for deltax, deltay in dirs:
                queue.append((i+deltax, j+deltay, total_step+1))
        
        return -1
            