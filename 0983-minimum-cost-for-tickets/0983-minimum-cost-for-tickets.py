class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        mem = [[None, None, None] for _ in range(len(days))]
        
        for i in range(len(mem)):
            if i == 0:
                mem[i][0] = costs[0]
                thirty_day = days[i] + 30 - 1
                seven_day = days[i] + 7 - 1
                j = i
                while j < len(days) and days[j] <= thirty_day:
                    if days[j] <= seven_day:
                        mem[j][1] = costs[1]
                    mem[j][2] = costs[2]
                    j += 1
            else:
                prev_min = min(mem[i-1])
                mem[i][0] = prev_min + costs[0]
                thirty_day = days[i] + 30 - 1
                seven_day = days[i] + 7 - 1
                j = i
                while j < len(days) and days[j] <= thirty_day:
                    if days[j] <= seven_day:
                        if mem[j][1] is None:
                            mem[j][1] = prev_min + costs[1]
                        else:
                            mem[j][1] = min(mem[j][1], prev_min + costs[1])
                    if mem[j][2] is None:
                        mem[j][2] = prev_min + costs[2]
                    else:
                        mem[j][2] = min(mem[j][2], prev_min + costs[2])
                    j += 1
        # print(mem)
                
        return min(mem[-1])