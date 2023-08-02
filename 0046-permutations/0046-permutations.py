class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            result = []
            
            for i in range(len(nums)):
                pivot = nums[i]
                remaining = nums[:i] + nums[i+1:]
                for p in self.permute(remaining):
                    result.append([nums[i], *p])
            
            return result