class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """
        delta_x = abs(sx - fx)
        delta_y = abs(sy - fy)
        if delta_x == delta_y == 0:
            return t != 1
        
        fastest_t = max(delta_x, delta_y)
        return t >= fastest_t