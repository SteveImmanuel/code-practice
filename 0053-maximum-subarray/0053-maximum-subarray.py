class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memory = [None] * len(nums)
        memory[0] = nums[0]

        for i in range(1, len(nums)):
            if memory[i-1] + nums[i] > nums[i]:
                memory[i] = memory[i-1] + nums[i]
            else:
                memory[i] = nums[i]
        return max(memory)