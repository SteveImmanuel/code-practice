class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        cur_sum = 0
        result = []
        for i in range(len(nums)):
            if i - k < 0 or i + k >= len(nums):
                result.append(-1)
                if i - k - 1 <= 0:
                    cur_sum += nums[i]
            else:
                if i - k - 1 < 0:
                    for j in range(i, i+k):
                        cur_sum += nums[j]
                else:
                    cur_sum -= nums[i-k-1]
                
                cur_sum += nums[i+k]
                result.append(cur_sum // (2 * k + 1))
        return result
                        
                