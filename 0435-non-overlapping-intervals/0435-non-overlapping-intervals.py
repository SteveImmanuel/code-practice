class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        # i = 0
        # total_remove = 0
        # while i < len(sorted_intervals) - 1:
        #     if sorted_intervals[i][1] > sorted_intervals[i+1][0]:
        #         total_remove += 1
        
        sorted_points = sorted(intervals, key=lambda x:(x[0], -x[1]))
        # print(sorted_points)
        
        i = 1
        total_shot = 1
        cur_range = [sorted_points[0][0], sorted_points[0][1]]
        while i < len(sorted_points):
            if cur_range[1] > sorted_points[i][0]:
                cur_range[0] = max(cur_range[0], sorted_points[i][0])
                cur_range[1] = min(cur_range[1], sorted_points[i][1])
            else:
                # print(cur_range)
                total_shot += 1
                cur_range = [sorted_points[i][0], sorted_points[i][1]]
            
            i += 1

        # return total_shot
        return len(intervals) - total_shot