class Solution:
    def rob(self, nums: List[int]) -> int:
#         mem = [None] * len(nums)
        
#         for i in range(len(nums)):
#             if i == 0:
#                 mem[i] = [(nums[i], True), (0, False)]
#             else:
#                 mem[i] = [None, None]
#                 mem[i][0] = (nums[i] + mem[i-1][1][0], mem[i-1][1][1])
#                 if mem[i-1][0][0] > mem[i-1][1][0]:
#                     mem[i][1] = (mem[i-1][0][0], mem[i-1][0][1])
#                 elif mem[i-1][0][0] < mem[i-1][1][0]:
#                     mem[i][1] = (mem[i-1][1][0], mem[i-1][1][1])
#                 else:
#                     mem[i][1] = (mem[i-1][0][0], mem[i-1][1][1] and mem[i-1][0][1])
                        
#         take, no_take = mem[-1]
#         print(mem)
#         res = nums[-1]
#         if take[0] > no_take[0] and not take[1]:
#             res = max(res, take[0]) 
#         else:
#             res = max(res, no_take[0]) 
#         return res
        if len(nums) == 1:
            return nums[0]

        mem1 = [None] * (len(nums) - 1)
        for i in range(len(nums) - 1):
            if i == 0:
                mem1[i] = (nums[i], 0)
            else:
                mem1[i] = (nums[i] + mem1[i-1][1], max(mem1[i-1]))
        
        mem2 = [None] * (len(nums) - 1)
        for i in range(len(nums) - 1):
            if i == 0:
                mem2[i] = (nums[i+1], 0)
            else:
                mem2[i] = (nums[i+1] + mem2[i-1][1], max(mem2[i-1]))
        
        print(mem1)
        print(mem2)
        
        return max(*mem1[-1], *mem2[-1])
        
        
        
        
        
        
        
        
        
        
        