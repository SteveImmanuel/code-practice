class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = []
        col_len = len(strs[0])
        
        for i in range(col_len):
            col = []
            for j in range(len(strs)):
                col.append(strs[j][i])
            cols.append(col)
        
        total_delete = 0
        for col in cols:
            if sorted(col) != col:
                total_delete += 1
        return total_delete