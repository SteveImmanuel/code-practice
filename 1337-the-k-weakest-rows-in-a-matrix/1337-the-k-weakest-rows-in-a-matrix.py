class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier_count = [(sum(mat[i]), i) for i in range(len(mat))]
        heapq.heapify(soldier_count)
        res = []
        for i in range(k):
            res.append(heapq.heappop(soldier_count)[1])
        return res