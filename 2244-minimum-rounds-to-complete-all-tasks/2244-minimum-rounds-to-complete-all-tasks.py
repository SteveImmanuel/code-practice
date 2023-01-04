class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        task_count = Counter(tasks)
        total_round = 0
        
        for occ in task_count.values():
            if occ == 1:
                return -1
            else:
                if occ % 3 == 0:
                    total_round += (occ // 3)
                else:
                    total_round += (occ // 3) + 1
        return total_round