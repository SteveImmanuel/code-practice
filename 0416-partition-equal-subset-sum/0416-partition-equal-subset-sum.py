class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        desired = total // 2
        mem = [[None for _ in range(desired + 1)] for _ in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(desired + 1):
                if j == 0 or nums[i] == j:
                    mem[i][j] = True
                else:
                    if nums[i] < j:
                        mem[i][j] = mem[i-1][j] or mem[i-1][j-nums[i]]
                    else:
                        mem[i][j] = mem[i-1][j]              
        
        return mem[-1][desired]