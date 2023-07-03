class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        diff_idx = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_idx.append(i)
        if len(diff_idx) > 2:
            return False
        elif len(diff_idx) == 0:
            occ = Counter(s)
            for val in occ.values():
                if val > 1:
                    return True
            return False
        elif len(diff_idx) == 1:
            return False
        else:
            return s[diff_idx[0]] == goal[diff_idx[1]] and s[diff_idx[1]] == goal[diff_idx[0]]