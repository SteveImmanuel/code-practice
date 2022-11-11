class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = 1
        ptr2 = 1
        current_num = nums[0]
        
        while ptr1 < len(nums):
            if nums[ptr1] != current_num:
                nums[ptr2] = nums[ptr1]
                current_num = nums[ptr1]
                ptr2 += 1
            ptr1 += 1
        
        return ptr2
            
        