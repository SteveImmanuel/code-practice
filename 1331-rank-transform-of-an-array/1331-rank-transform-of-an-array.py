class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = sorted(list(set(arr)))
        rank = {x: y + 1 for y, x in enumerate(rank)}
        return [rank[x] for x in arr]