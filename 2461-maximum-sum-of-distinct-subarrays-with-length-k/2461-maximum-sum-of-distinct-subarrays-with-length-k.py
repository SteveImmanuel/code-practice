class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        numset = set(nums[:k])
        occ = Counter(nums[:k])
        cursum = sum(nums[:k])

        if len(numset) == k:
            maxsum = sum(nums[:k])
        else:
            maxsum = 0
        # print(occ, numset, cursum, maxsum)
        
        for i in range(1, len(nums) - k + 1):
            cursum = cursum + nums[i+k-1] - nums[i-1]
            occ[nums[i-1]] -= 1
            occ[nums[i+k-1]] += 1
            if occ[nums[i-1]] == 0:
                numset.discard(nums[i-1])
            numset.add(nums[i+k-1])
            if len(numset) == k:
                maxsum = max(maxsum, cursum)
            # print(occ, numset, cursum, maxsum)
            
                
        return maxsum