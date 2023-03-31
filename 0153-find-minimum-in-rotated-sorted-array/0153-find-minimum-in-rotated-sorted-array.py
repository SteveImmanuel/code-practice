class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.find_min_lr(nums, 0, len(nums) - 1)
    
    def find_min_lr(self, nums, l, r):
        if nums[l] < nums[r] or l == r:
            return nums[l]
        else:
            m = (l + r) // 2
            min_left = self.find_min_lr(nums, l, m)
            min_right = self.find_min_lr(nums, m + 1, r)
            return min(min_left, min_right)