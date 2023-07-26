import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l, h = 1, 10000009
        while l < h:
            m = (l + h) // 2
            if self.total_time(dist, m) <= hour:
                h = m
            else:
                l = m + 1
        if self.total_time(dist, l) <= hour:
            return l
        return -1
    
    def total_time(self, dist, speed):
        time_spent = 0
        for i, d in enumerate(dist):
            duration = d / speed
            if i < len(dist) - 1:
                duration = math.ceil(duration)
            time_spent += duration
                
        return time_spent