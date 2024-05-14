DELTAS = [(0,1),(1,0),(0,-1),(-1,0)]
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                cur = self.dfs((i,j), 0, 0, set(), grid)
                res = max(res, cur)
        return res
    
    def dfs(self, pos, last_score, last_max, visited, grid):
        visited.add(pos)
        cur_score = last_score + grid[pos[0]][pos[1]]
        cur_max = max(cur_score, last_max)

        for dx, dy in DELTAS:
            next_pos = (pos[0]+dx, pos[1]+dy)
            if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[0]) or next_pos in visited or grid[next_pos[0]][next_pos[1]] == 0:
                continue
            next_max = self.dfs((pos[0]+dx, pos[1]+dy), cur_score, cur_max, visited, grid)
            cur_max = max(cur_max, next_max)
        
        visited.remove(pos)
        return cur_max
        