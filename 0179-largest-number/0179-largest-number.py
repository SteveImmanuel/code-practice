class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sort_nums = self.merge_sort(list(map(str, nums)))
        res = ''.join(sort_nums)
        start_idx = 0
        while start_idx < len(res) and res[start_idx] == '0':
            start_idx += 1
        if start_idx == len(res):
            start_idx -= 1
        return res[start_idx:]
    
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        
        m = len(nums) // 2
        left = self.merge_sort(nums[:m])
        right = self.merge_sort(nums[m:])
        return self.merge(left, right)
        
    def merge(self, nums1, nums2):
        res = []
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if self.is_greater_than(nums1[ptr1], nums2[ptr2]):
                res.append(nums1[ptr1])
                ptr1 += 1
            else:
                res.append(nums2[ptr2])
                ptr2 += 1
        while ptr1 < len(nums1):
            res.append(nums1[ptr1])
            ptr1 += 1
        while ptr2 < len(nums2):
            res.append(nums2[ptr2])
            ptr2 += 1
        return res
        
        
    def is_greater_than(self, num1, num2):
        alt1 = num1 + num2
        alt2 = num2 + num1
        ptr1, ptr2 = 0, 0
        while ptr1 < len(alt1) and ptr2 < len(alt2):
            if int(alt1[ptr1]) > int(alt2[ptr2]):
                return True
            elif int(alt1[ptr1]) < int(alt2[ptr2]):
                return False
            ptr1 += 1
            ptr2 += 1
        
        return False
            
