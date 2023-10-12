# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak_idx = self.findPeak(mountain_arr)
        print(peak_idx)
        
        l = 0
        r = peak_idx
        while l <= r:
            m = (l + r) // 2
            m_val = mountain_arr.get(m)
            if m_val == target:
                return m
            elif m_val > target:
                r = m - 1
            else:
                l = m + 1
        
        l = peak_idx
        r = mountain_arr.length() - 1
        while l <= r:
            m = (l + r) // 2
            m_val = mountain_arr.get(m)
            if m_val == target:
                return m
            elif m_val > target:
                l = m + 1
            else:
                r = m - 1
                
        return -1
        
    def findPeak(self, mountain_arr):
        l = 0
        r = mountain_arr.length() - 1
        while l < r:
            m = (l + r) // 2
            if mountain_arr.get(m) < mountain_arr.get(m+1):
                l = m + 1
            else:
                r = m
        return l