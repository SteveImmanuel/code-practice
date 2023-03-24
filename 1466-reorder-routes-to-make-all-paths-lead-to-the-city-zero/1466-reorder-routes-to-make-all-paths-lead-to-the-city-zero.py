class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connections_dict = defaultdict(list)
        
        for start, end in connections:
            connections_dict[start].append((end, True))
            connections_dict[end].append((start, False))
            
        total_change = 0
        queue = deque([0])
        visited = set()
        while len(queue) > 0:
            # print('b', queue)
            item = queue.popleft()
                
            visited.add(item)
            for neighbor in connections_dict[item]:
                # print('  ', item, neighbor)
                if neighbor[0] in visited:
                    continue
                else:
                    if neighbor[1]:
                        total_change += 1
                    queue.append(neighbor[0])
            # print('a', queue, total_change)
            
        
        return total_change
