class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = [[]]
        for i in range(1, len(sorted_nums) + 1):
             result += self.get_subset(sorted_nums, i)
        return result
                
        
    def get_subset(self, nums, length):
        if length == 1:
            return [[num] for num in set(nums)]
        else:
            has_seen = set()
            result = []
            
            for i in range(len(nums) - length + 1):
                pivot = nums[i]
                if pivot not in has_seen:
                    has_seen.add(pivot)
                    # print(pivot, nums[i+1:], length-1)
                    rest = self.get_subset(nums[i+1:], length - 1)
                    
                    for item in rest:
                        result.append([pivot] + item)
                    
            # print(nums, length, result)
            # print()
            return result