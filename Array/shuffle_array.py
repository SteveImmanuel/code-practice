# https://leetcode.com/problems/shuffle-an-array/
from itertools import count
from typing import List

class Solution:

    def factorial(self, x):
        if x == 1:
            return 1
        else:
            return x * self.factorial(x-1)

    def __init__(self, nums: List[int]):
        self.nums = nums      
        self.permutations = self.permutate(nums)
        self.total_permutations = self.factorial(len(nums))
        self.counter = 0


    def permutate(self, elements):
        if len(elements) <=1:
            yield elements
        else:
            for perm in self.permutate(elements[1:]):
                for i in range(len(elements)):
                    yield perm[:i] + elements[0:1] + perm[i:]

    def reset(self) -> List[int]:
        return self.nums        

    def shuffle(self) -> List[int]:
        if self.counter < self.total_permutations:
            self.counter += 1
        else:
            self.permutations = self.permutate(self.nums)
            self.counter = 1
        return next(self.permutations)

sol = Solution([1,2])