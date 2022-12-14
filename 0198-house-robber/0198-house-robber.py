class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [None] * len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                mem[i] = (nums[i], 0)
            else:
                mem[i] = (nums[i]+mem[i-1][1], max(mem[i-1]))
        return max(mem[-1])