class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        biggest = 0
        for i in range(len(points) - 1):
            biggest = max(biggest, points[i+1][0] - points[i][0])
        return biggest