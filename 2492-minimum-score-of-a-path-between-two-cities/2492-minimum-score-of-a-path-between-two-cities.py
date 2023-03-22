class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        neighbor_dict = defaultdict(list)
        for start, end, dist in roads:
            neighbor_dict[start].append((end, dist))
            neighbor_dict[end].append((start, dist))
        
        min_score = 100000
        queue = deque([(-1, 1, min_score)])
        visitation_set = set()
        while len(queue) > 0:
            item = queue.popleft()
            if (item[0], item[1]) in visitation_set or (item[1], item[0]) in visitation_set:
                continue
            
            visitation_set.add((item[0], item[1]))
            visitation_set.add((item[1], item[0]))
            min_score = min(min_score, item[2])
            for neighbor in neighbor_dict[item[1]]:
                queue.append((item[1], neighbor[0], neighbor[1]))
        
        return min_score
            
            
        
