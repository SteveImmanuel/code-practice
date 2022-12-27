class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        need_addition = []
        for i in range(len(capacity)):
            need_addition.append(capacity[i] - rocks[i])
        need_addition.sort()
        
        total_full_bag = 0
        remaining_rocks = additionalRocks
        for i in range(len(need_addition)):
            if need_addition[i] == 0:
                total_full_bag += 1
            else:
                if remaining_rocks > 0 and need_addition[i] <= remaining_rocks:
                    total_full_bag += 1
                    remaining_rocks -= need_addition[i]
        
        return total_full_bag