class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for asteroid in asteroids:
            size = abs(asteroid)
            if asteroid > 0:
                result.append(asteroid)
            else:
                while len(result) > 0 and result[-1] > 0 and abs(result[-1]) < size:
                    result.pop()
                if len(result) == 0 or result[-1] < 0:
                    result.append(asteroid)
                elif abs(result[-1]) == size:
                    result.pop()
                    
                    
        
        return result