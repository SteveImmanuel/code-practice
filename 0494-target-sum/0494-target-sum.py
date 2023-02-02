class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        max_sum = sum([abs(num) for num in nums])
        if not (-max_sum <= target <= max_sum):
            return 0
        
        mem = [[0 for _ in range(max_sum * 2 + 1)] for _ in range(len(nums))]
    
        for i in range(len(nums)):
            for j in range(max_sum * 2 + 1):
                cur_sum = j - max_sum
                if i == 0:
                    # print(cur_sum, nums[i], -nums[i])
                    if cur_sum == 0 and nums[i] == 0:
                        mem[i][j] = 2
                    elif cur_sum == nums[i] or cur_sum == -nums[i]:
                        mem[i][j] = 1
                    else:
                        mem[i][j] = 0
                else:
                    if -max_sum <= cur_sum + nums[i] <= max_sum:
                        # print(nums[i], cur_sum, cur_sum + nums[i], cur_sum + nums[i] + max_sum)
                        mem[i][j] += mem[i-1][cur_sum + nums[i] + max_sum]
                    if -max_sum <= cur_sum - nums[i] <= max_sum:
                        # print(nums[i], cur_sum, cur_sum - nums[i], cur_sum - nums[i] + max_sum)
                        mem[i][j] += mem[i-1][cur_sum - nums[i] + max_sum]
            # print(mem[i])
        return mem[-1][target + max_sum]