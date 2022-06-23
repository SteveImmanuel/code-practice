# https://leetcode.com/problems/max-points-on-a-line/

from typing import List
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        max_len = -1
        for i in range(len(points)):
            pivot = points[i]
            rest = points[:i] + points[i+1:]

            grad_dict = defaultdict(int)
            for point in rest:
                grad_dict[self.gradient(pivot, point)] += 1
            
            cur_max = max(grad_dict.values())
            max_len = max(max_len, cur_max)

        return max_len + 1        
            

    def gradient(self, point1, point2):
        if point2[0] - point1[0] == 0:
            return 'inf'
        return (point2[1]-point1[1])/(point2[0]-point1[0])

sol = Solution()
points = [[i,i] for i in range(1)]
print(sol.maxPoints(points))