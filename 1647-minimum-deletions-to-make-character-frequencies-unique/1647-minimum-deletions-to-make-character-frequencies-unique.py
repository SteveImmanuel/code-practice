class Solution:
    def minDeletions(self, s: str) -> int:
        occ = Counter(s)
        rev_occ = defaultdict(list)
        for key in occ:
            rev_occ[occ[key]].append(key)
        rev_occ = list(rev_occ.items())
        rev_occ.sort()
        available = [i for i in range(1, rev_occ[0][0])]
        total_delete = 0
        for i in range(len(rev_occ)):
            if len(rev_occ[i][1]) > 1:
                for j in range(len(rev_occ[i][1]) - 1):
                    slot = 0
                    if len(available) > 0:
                        slot = available.pop()
                    total_delete += rev_occ[i][0] - slot
                
            if i < len(rev_occ) - 1:
                available += [k for k in range(rev_occ[i][0] + 1, rev_occ[i+1][0])]
        
        return total_delete