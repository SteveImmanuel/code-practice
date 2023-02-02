class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occ = {}
        for idx, c in enumerate(s):
            if c not in occ:
                occ[c] = [idx, idx]
            else:
                occ[c][1] = idx
        print(occ)
        intervals = list(occ.values())
        intervals.sort(key=lambda x:x[0])
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                if intervals[i+1][1] > intervals[i][1]:
                    intervals[i][1] = intervals[i+1][1]
                intervals.pop(i+1)
            else:
                i += 1
        res = [b-a+1 for a,b in intervals]
        return res