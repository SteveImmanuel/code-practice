# https://leetcode.com/problems/course-schedule-ii/
from typing import List

class Solution:
    # TIME LIMIT EXCEEDED
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    #     req_dict = {i:set() for i in range(numCourses)}
    #     for course, prereq in prerequisites:
    #         req_dict[course].add(prereq)
    #     return self.findOrderRec(req_dict, [])

    # def findOrderRec(self, req_dict, current_order):
    #     if len(req_dict) == 0:
    #         return current_order

    #     candidates = []
    #     for key, val in req_dict.items():
    #         if len(val) == 0:
    #             candidates.append(key)


    #     for candidate in candidates:
    #         temp_req_dict = req_dict.copy()
    #         temp_current_order = current_order.copy()


    #         temp_current_order.append(candidate)
    #         del temp_req_dict[candidate]
    #         for key in temp_req_dict.keys():
    #             temp_req_dict[key].discard(candidate)

    #         res = self.findOrderRec(temp_req_dict, temp_current_order)
    #         if res != []:
    #             return res

    #     return []

    # ACCEPTED, but kinda slow O(n^2)
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    #     req_dict = {i:set() for i in range(numCourses)}
    #     for course, prereq in prerequisites:
    #         req_dict[course].add(prereq)

    #     current_order = []
    #     candidates = []
    #     for key, val in req_dict.items():
    #         if len(val) == 0:
    #             candidates.append(key)

    #     while candidates != []:
    #         current_order += candidates

    #         for candidate in candidates:
    #             del req_dict[candidate]
    #             for values in req_dict.values():
    #                 values.discard(candidate)
            
    #         candidates = []
    #         for key, val in req_dict.items():
    #             if len(val) == 0:
    #                 candidates.append(key)

        
    #     if len(req_dict) == 0:
    #         return current_order
    #     else:
    #         return []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        req_dict = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            req_dict[prereq].append(course)
        is_visited = [False] * numCourses
        recursion_stack = [False] * numCourses
        result = []

        for key in req_dict.keys():
            self.findOrderRec(key, is_visited, req_dict, result, recursion_stack)
        
        if len(result) == numCourses:
            return result[::-1]
        return []

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
prerequisites = [[1,0],[2,0],[3,1],[3,2],[0,3]]
print(sol.findOrder(numCourses, prerequisites))