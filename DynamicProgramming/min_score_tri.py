# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
# NOT DONE
from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        if len(values) < 3:
            return 0

        min_score = None
        memory = {}
        memory2 = {}
        print('minscoretriangle', memory, memory2)

        for i in range(len(values)):
            if i not in memory:

                current_anchor = i
                last_anchor = current_anchor + 2
                current_score = 0
                new_val = [values[current_anchor]]

                while (current_anchor < last_anchor < len(values)) or (last_anchor - len(values) <= i):
                    temp_idx = last_anchor % len(values)
                    if temp_idx != i:
                        new_val.append(values[last_anchor % len(values)])
                    # print(current_anchor, last_anchor)
                    tri_score = 1
                    for k in range(current_anchor, last_anchor + 1):
                        tri_score *= values[k % len(values)]
                    print(tri_score)
                    current_score += tri_score

                    current_anchor = last_anchor
                    last_anchor = current_anchor + 2
                
                # new_val = [values[k] for k in range(i, len(values), 2)]
                print('mem2', memory2, new_val, i, i not in memory2)
                if i not in memory2:
                    additional = self.minScoreTriangulation(new_val)

                    for k in range(i, len(values), 2):
                        memory2[k] = additional
                
                for k in range(i, len(values), 2):
                    memory[k] = current_score + memory2[k]
                print('final score', memory[k])
            if min_score is None or min_score > memory[k]:
                min_score = memory[k]
            print('current', memory, memory2)
        print(memory, memory2)

        
        return min_score

sol = Solution()
x = [2,2,2,2,1]
print(sol.minScoreTriangulation(x))