class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        cost_dict_node1 = {}
        cost_dict_node2 = {}
        
        visited = [False] * n
        queue = deque([(node1, 0)])
        while len(queue) > 0:
            cur_node, cost = queue.popleft()
            if visited[cur_node] or cur_node == -1:
                continue
                
            visited[cur_node] = True
            cost_dict_node1[cur_node] = cost
            queue.append((edges[cur_node], cost + 1))
        
        visited = [False] * n
        queue = deque([(node2, 0)])
        while len(queue) > 0:
            cur_node, cost = queue.popleft()
            if visited[cur_node] or cur_node == -1:
                continue
                
            visited[cur_node] = True
            cost_dict_node2[cur_node] = cost
            queue.append((edges[cur_node], cost + 1))
            
        # print(cost_dict_node1)
        # print(cost_dict_node2)

        idx = -1
        cost = None
        for i in range(n):
            if i not in cost_dict_node1 or i not in cost_dict_node2:
                continue
            
            if cost is None or max(cost_dict_node1[i], cost_dict_node2[i]) < cost:
                cost = max(cost_dict_node1[i], cost_dict_node2[i])
                idx = i
        return idx