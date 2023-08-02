class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        gen = self.permute_gen([i for i in range(1, n+1)])
        while k > 0:
            res = next(gen)
            k -= 1
        return ''.join(map(str, res))
        
        
    def permute_gen(self, nums):
        if len(nums) == 1:
            yield nums
        else:
            result = []
            
            for i in range(len(nums)):
                pivot = nums[i]
                remaining = nums[:i] + nums[i+1:]
                for p in self.permute_gen(remaining):
                    yield [nums[i], *p]
                    # result.append([nums[i], *p])
            
            # return result