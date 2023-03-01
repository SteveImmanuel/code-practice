class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)
    
    def mergearr(self, arr1, arr2):
        i = 0
        j = 0
        res = []
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        while i < len(arr1):
            res.append(arr1[i])
            i += 1
        while j < len(arr2):
            res.append(arr2[j])
            j += 1
        return res
    
    def mergesort(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.mergesort(nums[:mid])
        right = self.mergesort(nums[mid:])
        return self.mergearr(left, right)
        
        
    
    def quicksort(self, nums):      
        pivot = len(nums) // 2
        left = []
        right = []
        for i in range(len(nums)):
            if i == pivot:
                continue
                
            if nums[i] < nums[pivot]:
                left.append(nums[i])
            else: 
                right.append(nums[i])
        # print(nums, pivot, left, right)
        
        if len(left) > 0:
            left = self.quicksort(left)
        if len(right) > 0:
            right = self.quicksort(right)
        
        return left + [nums[pivot]] + right