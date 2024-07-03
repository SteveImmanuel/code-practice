class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 4:
            return 0
        
        delta = len(nums) - 4
        res = float('inf')
        for i in range(0, len(nums) - delta):
            res = min(res, nums[i + delta] - nums[i])
        return res