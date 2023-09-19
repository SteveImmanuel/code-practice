class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        turtle = nums[0]
        hare = nums[0]
        
        while True:
            turtle = nums[turtle]
            hare = nums[nums[hare]]
            
            if turtle == hare:
                break
                
        hare = nums[0]
        while hare != turtle:
            hare = nums[hare]
            turtle = nums[turtle]
        
        return hare