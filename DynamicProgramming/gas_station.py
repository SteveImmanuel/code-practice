# https://leetcode.com/problems/gas-station/

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        candidate_start = []
        for i in range(len(gas)):
            if cost[i] <= gas[i]:
                candidate_start.append(i)

        if len(candidate_start) == 0:
            return -1

        memory = {}
        while len(candidate_start) > 0:
            candidate = candidate_start.pop()
            end_idx, _ = self.traverse_gas(gas[candidate], candidate, gas, cost, memory)
            if end_idx == candidate:
                return candidate
        
        return -1

    def traverse_gas(self, initial_gas, start_idx, gas, cost, memory):
        current_idx = (start_idx + 1) % len(gas)
        current_gas = initial_gas - cost[start_idx] + gas[current_idx]

        is_valid = True
        while is_valid and current_idx != start_idx:
            if current_idx in memory:
                m_init_gas, m_current_idx, m_current_gas = memory[current_idx]
                if current_gas >= m_init_gas:
                    current_idx = m_current_idx
                    current_gas = m_current_gas + (current_gas - m_init_gas)
                else:
                    is_valid = False
            else:
                if current_gas >= cost[current_idx]:
                    next_idx = (current_idx + 1) % len(gas)
                    current_gas = current_gas - cost[current_idx] + gas[next_idx]
                    current_idx = next_idx
                else:
                    is_valid = False
        
        memory[start_idx] = (initial_gas, current_idx, current_gas)
        return current_idx, current_gas

sol = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(sol.canCompleteCircuit(gas, cost))