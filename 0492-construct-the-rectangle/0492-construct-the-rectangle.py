import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        start = int(math.ceil(area ** 0.5))
        for i in range(start, area + 1):
            div, mod = divmod(area, i)
            if mod == 0:
                return [i, div]