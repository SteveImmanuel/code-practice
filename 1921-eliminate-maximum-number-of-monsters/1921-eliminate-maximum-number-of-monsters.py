import math

class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        timestep = []
        for d, s in zip(dist, speed):
            timestep.append(math.ceil(float(d) / float(s)))
        timestep.sort()
        
        elapsed = 0
        total_kill = 0
        first = True
        for t in timestep:
            if elapsed < t or first:
                total_kill += 1
            else:
                break
            elapsed += 1
            first = False
        return total_kill
        