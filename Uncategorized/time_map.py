# https://leetcode.com/problems/time-based-key-value-store/
from bisect import bisect_right
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.data = defaultdict(lambda: [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))      

    def get(self, key: str, timestamp: int) -> str:
        biggest_key_idx = self._bisect_right(key, timestamp)
        if biggest_key_idx == 0:
            return ''
        
        return self.data[key][biggest_key_idx-1][1]
    
    def _bisect_right(self, key, timestamp):
        l, h = 0, len(self.data[key])

        while l < h:
            mid = (l+h) // 2
            if self.data[key][mid][0] <= timestamp:
                l = mid+1
            else:
                h = mid
        return l
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)