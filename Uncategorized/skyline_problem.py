# https://leetcode.com/problems/the-skyline-problem/description/

from typing import List
from collections import deque
class Solution:
    def insert_height(self, height_arr, height):
        lo_left, hi_left = 0, len(height_arr)
        while lo_left < hi_left:
            mid = lo_left + (hi_left - lo_left) // 2
            if height_arr[mid][2] > height[2]:
                lo_left = mid + 1
            else: 
                hi_left = mid
        
        lo_right, hi_right = 0, len(height_arr)
        while lo_right < hi_right:
            mid = lo_right + (hi_right - lo_right) // 2
            if height_arr[mid][2] >= height[2]:
                lo_right = mid + 1
            else:
                hi_right = mid

        if lo_left == len(height_arr):
            height_arr.append(height)
        elif lo_left == len(height_arr):
            height_arr.appendLeft(height)
        else:
            if height_arr[lo_left][2] == height[2]:

                lo, hi = lo_left, lo_right
                while lo < hi:
                    mid = lo + (hi - lo) // 2
                    if height_arr[mid][1] < height[1]:
                        lo = mid + 1
                    else:
                        hi = mid
                
                height_arr.insert(lo, height)
            else:
                height_arr.insert(lo_left, height)


    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        height_arr = deque()
        queue = deque(buildings)
        
        res = []
        current_left = 0
        while len(queue) > 0 or len(height_arr) > 0:
            queue_pop = False
            if len(queue) > 0 and len(height_arr) > 0:
                if queue[0][0] <= height_arr[0][1]:
                    queue_pop = True
                # else:
                #     item = height_arr.popleft()
            elif len(queue) > 0:
                queue_pop = True
                # item = queue.popleft()
            # else:
            #     item = height_arr.popleft()

            if queue_pop:
                left, right, height = queue.popleft()
                max_height = 0
                if len(height_arr) > 0:
                    max_height = height_arr[0][2]

                if height > max_height:
                    if len(height_arr) > 0 and left == height_arr[0][0]:
                        res[-1][1] = height
                    else:
                        res.append([left, height])

                self.insert_height(height_arr, [left, right, height])
                current_left = left
            else:
                _, pos, height = height_arr.popleft()
                if current_left <= pos:
                    next_height = 0
                    
                    while len(height_arr) > 0 and height_arr[0][1] <= pos:
                        height_arr.popleft()

                    if len(height_arr) > 0:
                        next_height = height_arr[0][2]
                    if height > next_height:
                        res.append([pos, next_height])
                    current_left = pos
            
        return res

                            


sol = Solution()
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# buildings = [[0,2,3],[2,5,3]]
# buildings = [[1,2,1],[1,2,2],[1,2,3]]
# buildings = [[0,3,3],[1,5,3],[2,4,3],[3,7,3]]
buildings = [[1,38,219],[2,19,228],[2,64,106],[3,80,65],[3,84,8],[4,12,8],[4,25,14],[4,46,225],[4,67,187],[5,36,118],[5,48,211],[5,55,97],[6,42,92],[6,56,188],[7,37,42],[7,49,78],[7,84,163],[8,44,212],[9,42,125],[9,85,200],[9,100,74],[10,13,58],[11,30,179],[12,32,215],[12,33,161],[12,61,198],[13,38,48],[13,65,222],[14,22,1],[15,70,222],[16,19,196],[16,24,142],[16,25,176],[16,57,114],[18,45,1],[19,79,149],[20,33,53],[21,29,41],[23,77,43],[24,41,75],[24,94,20],[27,63,2],[31,69,58],[31,88,123],[31,88,146],[33,61,27],[35,62,190],[35,81,116],[37,97,81],[38,78,99],[39,51,125],[39,98,144],[40,95,4],[45,89,229],[47,49,10],[47,99,152],[48,67,69],[48,72,1],[49,73,204],[49,77,117],[50,61,174],[50,76,147],[52,64,4],[52,89,84],[54,70,201],[57,76,47],[58,61,215],[58,98,57],[61,95,190],[66,71,34],[66,99,53],[67,74,9],[68,97,175],[70,88,131],[74,77,155],[74,99,145],[76,88,26],[82,87,40],[83,84,132],[88,99,99]]
print(sol.getSkyline(buildings))