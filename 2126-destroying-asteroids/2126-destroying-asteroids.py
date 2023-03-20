class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        sorted_asteroids = sorted(asteroids)
        total_mass = mass
        i = 0
        while i < len(sorted_asteroids):
            if total_mass >= sorted_asteroids[i]:
                total_mass += sorted_asteroids[i]
                i += 1
            else:
                break
                
        return i == len(sorted_asteroids)