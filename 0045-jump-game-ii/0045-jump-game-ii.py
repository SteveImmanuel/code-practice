class Solution:
    def jump(self, nums: List[int]) -> int:
        mem = [None for i in range(len(nums))]
        
        mem[0] = 0
        for i in range(len(nums)):
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                if mem[j] is None:
                    mem[j] = mem[i] + 1
                else:
                    mem[j] = min(mem[i] + 1, mem[j])
        # print(mem)
        return mem[-1]