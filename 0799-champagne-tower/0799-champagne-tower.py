class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        mem = {}
        res, _ = self.get_condition(query_row, query_glass, poured, mem)
        # print(mem)
        return res
    
    def get_condition(self, row, glass, poured, mem):
        key = (row, glass)
        if key not in mem:
            if row == 0:
                fill = poured
            else:
                if glass == 0:
                    parent_idx = [glass]
                elif glass == row:
                    parent_idx = [glass-1]
                else:
                    parent_idx = [glass-1, glass]
                
                fill = 0.0
                for idx in parent_idx:
                    cond, excess = self.get_condition(row - 1, idx, poured, mem)
                    fill += excess / 2
                    
            if fill >= 1:
                condition = (1, fill - 1.0)
            else:
                condition = (fill, 0)
            
            mem[key] = condition
        
        return mem[key]