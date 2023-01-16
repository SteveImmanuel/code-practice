class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = intervals.copy()
        result.append(newInterval)
        result.sort(key=lambda x: x[0])

        i = 0
        while i < len(result) - 1:
            if result[i][1] >= result[i+1][0]:
                if result[i][1] <= result[i+1][1]:
                    result[i][1] = result[i+1][1]

                result.pop(i+1)
            else:
                i += 1
        
        return result