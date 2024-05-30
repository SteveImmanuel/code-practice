class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_occ = defaultdict(int)
        cur_color = {}
        ans = []
        for idx, color in queries:
            if idx in cur_color:
                old_color = cur_color[idx]
                color_occ[old_color] -= 1
                if color_occ[old_color] == 0:
                    del color_occ[old_color]
            cur_color[idx] = color
            color_occ[color] += 1
            ans.append(len(color_occ))
        return ans