class Solution:
    def partitionString(self, s: str) -> int:
        cur_set = set()
        total_partition = 1
        
        for c in s:
            if c not in cur_set:
                cur_set.add(c)
            else:
                #print(cur_set, c)
                
                total_partition += 1
                cur_set = set([c])
        
        return total_partition