class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank_heap = [(s, i) for i, s in enumerate(score)]
        heapq.heapify(rank_heap)
        
        res = [None] * len(score)
        rank_dict = {1:'Gold Medal', 2:'Silver Medal', 3:'Bronze Medal'}
        while len(rank_heap) > 0:
            rank = rank_dict.get(len(rank_heap), str(len(rank_heap)))
            _, player_idx = heapq.heappop(rank_heap)
            res[player_idx] = rank
        return res