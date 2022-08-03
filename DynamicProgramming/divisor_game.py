# https://leetcode.com/problems/divisor-game/
from typing import List

class Solution:
    def get_possible_x(self, n):
        pos = [1]
        for i in range(2, int((n**0.5)//1) + 1):
            if n%i == 0:
                pos.append(i)
                pos.append(int(n//i))
        return pos

    def divisorGame(self, n: int) -> bool:
        outcome = [None] * n
        outcome[0] = False
        for i in range(2, n+1):
            possible_x = self.get_possible_x(i)
            # print(i, possible_x)
            for x in possible_x:
                if not outcome[i - x - 1]:
                    outcome[i - 1] = True
                    break
                else:
                    outcome[i - 1] = False
        return outcome[-1]

sol = Solution()
# for i in range(1,10):
print(sol.divisorGame(1000))