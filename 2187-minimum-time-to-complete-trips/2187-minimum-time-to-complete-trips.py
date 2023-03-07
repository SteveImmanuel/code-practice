class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        max_time = max(time)
        l = 1
        h = max_time * totalTrips
        
        while l < h:
            m = (l + h) // 2
            cur_trip = self.calculate_total_trips(time, m)
            # print(l, m, h, cur_trip)
            if cur_trip < totalTrips:
                l = m + 1
            else:
                h = m
        return l
    
    def calculate_total_trips(self, time, cur_timestamp):
        total = 0
        for bus in time:
            total += cur_timestamp // bus
        return total