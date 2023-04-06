class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_heap = [i for i in range(n)]
        meeting_deque = deque(sorted(meetings, key=lambda x: x[0]))
        
        heapq.heapify(room_heap)
        room_dealloc_heap = []
        room_usage = [0] * n
        current_time = 0
        
        while len(meeting_deque) > 0:
            meeting = meeting_deque[0]
            if current_time <= meeting[0]:
                while len(room_dealloc_heap) > 0 and room_dealloc_heap[0][0] <= meeting[0]:
                    dealloc_room = heapq.heappop(room_dealloc_heap)
                    heapq.heappush(room_heap, dealloc_room[1])
                current_time = meeting[0]

            # print(current_time, 'meeting', meeting_deque, 'room', room_heap, 'dealloc', room_dealloc_heap)
            if len(room_heap) > 0:
                meeting_deque.popleft()
                room = heapq.heappop(room_heap)
                # print('meeting', meeting, 'using room', room, 'will be available at', current_time + meeting[1] - meeting[0])
                room_usage[room] += 1
                heapq.heappush(room_dealloc_heap, (current_time + meeting[1] - meeting[0], room))
            else:
                dealloc_room = heapq.heappop(room_dealloc_heap)
                heapq.heappush(room_heap, dealloc_room[1])
                current_time = max(current_time, dealloc_room[0])
            # print()
        max_idx = 0
        for i in range(n):
            if room_usage[i] > room_usage[max_idx]:
                max_idx = i
        return max_idx