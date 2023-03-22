class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_dict = defaultdict(list)
        for course, prereq in prerequisites:
            prereq_dict[course].append(prereq)
            
        can_take_course = [None] * numCourses
        is_course_checked = [False] * numCourses
        
        i = 0
        while i < numCourses and self.can_take(i, prereq_dict, can_take_course, is_course_checked):
            i += 1
        # print(can_take_course)
        return i == numCourses
            
        
    def can_take(self, course, prereq_dict, can_take_course, is_course_checked):            
        # print(course, can_take_course[course])
        if can_take_course[course] is None:
            if is_course_checked[course]:
                return False
            else:
                is_course_checked[course] = True
                if len(prereq_dict[course]) == 0:
                    can_take_course[course] = True
                else:
                    can_take = True
                    for prereq in prereq_dict[course]:
                        can_take = can_take and self.can_take(prereq, prereq_dict, can_take_course, is_course_checked)
                        if not can_take:
                            break
                    can_take_course[course] = can_take
            
        return can_take_course[course]
        