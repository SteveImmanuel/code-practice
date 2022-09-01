# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List
class Solution:
    # Onlogn, bin search
    # can be o(n) using two pointer approach
    def find_idx(self, numbers, target):
        low = 0
        high = len(numbers)
        while low < high:
            mid = (low+high)//2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                low = mid + 1
            else:
                high = mid
            
        return -1
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            find_el = target - num
            find_el_idx = self.find_idx(numbers, find_el)
            print(find_el, find_el_idx)
            if find_el_idx != i and find_el_idx!=-1:
                return [min(i+1, find_el_idx+1), max(i+1, find_el_idx+1)]

sol = Solution()
numbers = [5,25,75]
target = 100
print(sol.twoSum(numbers, target))        