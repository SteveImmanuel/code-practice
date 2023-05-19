class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        set_dict = {0: set(), 1: set()}
        
        nodes_with_neighbor = []
        for i in range(len(graph)):
            if len(graph[i]) > 0:
                nodes_with_neighbor.append(i)
        
        nodes_with_neighbor = set(nodes_with_neighbor)
        while len(nodes_with_neighbor) > 0:
            queue = deque([(nodes_with_neighbor.pop(), 0)])
            while queue:
                item = queue.popleft()

                if item[0] not in set_dict[0] and item[0] not in set_dict[1]:
                    set_dict[item[1]].add(item[0])
                elif (item[0] in set_dict[item[1]]) and (item[0] not in set_dict[1 - item[1]]):
                    continue            
                else:
                    return False
                
                nodes_with_neighbor.discard(item[0])

                for node in graph[item[0]]:
                    queue.append((node, 1 - item[1]))
        
        return True
                    