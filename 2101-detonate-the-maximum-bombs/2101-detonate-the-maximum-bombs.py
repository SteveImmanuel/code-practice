class Solution:
    def is_in_range(self, bomb1, bomb2):
        center_diff = (bomb1[0]-bomb2[0]) ** 2 + (bomb1[1]-bomb2[1]) ** 2
        return center_diff <= bomb1[2] ** 2
        
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bomb_connection = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j and self.is_in_range(bombs[i], bombs[j]):
                    bomb_connection[i].append(j)

        max_exploded = 0
        for i in range(len(bombs)):
            visited = set()
            queue = deque([i])
            while queue:
                item = queue.popleft()
                if item in visited:
                    continue
                visited.add(item)
                for other in bomb_connection[item]:
                    queue.append(other)
            total_exploded = len(visited)
            max_exploded = max(max_exploded, total_exploded)
            
        return max_exploded