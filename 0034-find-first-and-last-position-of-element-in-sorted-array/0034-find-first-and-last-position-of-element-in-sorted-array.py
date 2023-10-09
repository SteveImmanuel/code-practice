class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        found, l = self.bisect_left(nums, target)
        found, r = self.bisect_right(nums, target)
        if found:
            return [l, r - 1]
        return [-1, -1]
        
    def bisect_left(self, nums, target):
        l, r = 0, len(nums)
        found = False
        while l < r:
            m = (l + r) // 2
            
            if nums[m] == target:
                found = True
            # print(l, r, m, nums[l], nums[r], nums[m])
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        
        return found, l
    
    def bisect_right(self, nums, target):
        l, r = 0, len(nums)
        found = False
        while l < r:
            m = (l + r) // 2
            
            if nums[m] == target:
                found = True
            
            if nums[m] <= target:
                l = m + 1
            else:
                r = m
        
        return found, l