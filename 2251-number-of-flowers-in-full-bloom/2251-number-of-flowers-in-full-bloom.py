class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start_asc = sorted(map(lambda x: x[0], flowers))
        end_asc = sorted(map(lambda x: x[1], flowers))
        
        answer = []
        for p in people:
            start_bloom_idx = bisect_right(start_asc, p)
            end_bloom_idx = bisect_left(end_asc, p)            
            answer.append(start_bloom_idx - end_bloom_idx)
            # print(p, start_bloom_idx, end_bloom_idx)
        return answer