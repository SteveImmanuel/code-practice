# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
from typing import List
from collections import defaultdict
from bisect import bisect_left
import heapq
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        prop_dict = defaultdict(lambda: [])
        for attack, defense in properties:
            heapq.heappush(prop_dict[attack], -defense)

        attack_sorted = sorted(list(prop_dict.keys()))
        heap = []
        max_for_group = {}
        for i in range(len(attack_sorted)-1, -1, -1):
            if i == len(attack_sorted)-1:
                heap = prop_dict[attack_sorted[i]]
            else:
                max_val = -heapq.heappop(heap)
                heapq.heappush(heap, -max_val)
                max_for_group[attack_sorted[i]] = max_val

                for neg_defense in prop_dict[attack_sorted[i]]:
                    heapq.heappush(heap, neg_defense)
            
        # print(max_for_group)
        
        # print(prop_dict)
        # print(max_each_group)
        total_weak = 0
        for i in range(len(attack_sorted) - 1):
            pivot = attack_sorted[i]
            items = prop_dict[pivot]

            for item in items:
                if max_for_group[pivot] > -item:
                    # print(pivot, item)
                    total_weak += 1
        return total_weak


sol = Solution()
# properties = [[5,5],[6,3],[3,6]]
# properties = [[2,2],[3,3]]
# properties = [[1,5],[10,4],[4,3]]
properties = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]
print(sol.numberOfWeakCharacters(properties))