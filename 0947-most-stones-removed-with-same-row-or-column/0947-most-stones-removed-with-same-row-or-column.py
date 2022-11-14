class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        visitation_map = {(stone[0], stone[1]): False for stone in stones}
        stone_col = defaultdict(list)
        stone_row = defaultdict(list)
        
        for i, j in stones:
            stone_row[i].append(j)
            stone_col[j].append(i)

        total_union = 0
        for i,j in stones:
            if not visitation_map[(i,j)]:
                total_union += 1
                self.DFS(i, j, visitation_map, stone_row, stone_col)
                    
        return len(stones) - total_union

    def DFS(self, i, j, visitation_map, stone_row, stone_col):
        key = (i,j)
        if visitation_map[key]:
            return
        
        visitation_map[key] = True
        # dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        for col in stone_row[i]:
            self.DFS(i, col, visitation_map, stone_row, stone_col)

        for row in stone_col[j]:
            self.DFS(row, j, visitation_map, stone_row, stone_col)