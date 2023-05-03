class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        bus_dict = defaultdict(list)
        bus = [None for _ in range(len(routes))]
        
        for i, route in enumerate(routes):
            bus[i] = set(route)
            for stop in route:
                bus_dict[stop].append(i)
        
        queue = deque([(bus_num, 1) for bus_num in bus_dict[source]])
        bus_visited = [False for _ in range(len(bus))]
        while len(queue) > 0:
            # print(queue)
            bus_num, cost = queue.popleft()
            
            if bus_visited[bus_num]:
                continue
            
            bus_visited[bus_num] = True
            if target in bus[bus_num]:
                return cost
            
            for stop in bus[bus_num]:
                for trf_bus in bus_dict[stop]:
                    if trf_bus != bus_num:
                        queue.append((trf_bus, cost + 1))
        
        return -1