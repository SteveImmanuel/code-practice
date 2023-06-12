class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start_range = None
        end_range = None
        for i in range(len(nums)):
            if start_range is None:
                start_range = nums[i]
                end_range = nums[i]
            else:
                if nums[i] == nums[i-1] + 1:
                    end_range = nums[i]
                else:
                    if start_range != end_range:
                        result.append(f'{start_range}->{end_range}')
                    else:
                        result.append(f'{start_range}')                        
                    
                    start_range = nums[i]
                    end_range = nums[i]
        if start_range is not None:
            if start_range != end_range:
                result.append(f'{start_range}->{end_range}')
            else:
                result.append(f'{start_range}')
        return result