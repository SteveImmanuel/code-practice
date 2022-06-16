# https://leetcode.com/problems/course-schedule-i/
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        req_dict = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            req_dict[prereq].append(course)
        is_visited = [False] * numCourses
        recursion_stack = [False] * numCourses
        result = []

        for key in req_dict.keys():
            if not self.findOrderRec(key, is_visited, req_dict, result, recursion_stack):
                return False

        return True

    def findOrderRec(self, course, is_visited, req_dict, result, recursion_stack) -> List[int]:
        if not recursion_stack[course]:
            recursion_stack[course] = True
            if not is_visited[course]:
                for next_course in req_dict[course]:
                    if not self.findOrderRec(next_course, is_visited, req_dict, result, recursion_stack):
                        return False
                is_visited[course] = True
                result.append(course)
            recursion_stack[course] = False
            return True
        else:
            return False
            


        
sol = Solution()
numCourses = 5
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(sol.canFinish(numCourses, prerequisites))