class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited_rooms = [False] * n
        key_set = set([0])
        
        room_queue = deque([0])
        while len(room_queue) > 0:
            cur_room = room_queue.popleft()
            if visited_rooms[cur_room]:
                continue
                
            visited_rooms[cur_room] = True
            for key in rooms[cur_room]:
                key_set.add(key)
                room_queue.append(key)
        
        # print(key_set)
        return len(key_set) == n