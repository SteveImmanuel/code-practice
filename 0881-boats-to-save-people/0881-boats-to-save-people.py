class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people_sorted = sorted(people)
        l, r = 0, len(people) - 1
        total_boats = 0
        
        while l <= r:
            if people_sorted[r] == limit:
                r -= 1
                total_boats += 1
            else: # people_sorted[r] < limit
                if people_sorted[l] <= limit - people_sorted[r]:
                    l += 1
                r -= 1
                total_boats += 1
        return total_boats
        