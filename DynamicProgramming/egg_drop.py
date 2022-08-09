# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/
class Solution:
    def twoEggDrop(self, n: int) -> int:
        mem = [None] * n

        for i in range(n):
            if i == 0:
                mem[i] = 1
            else:
                for j in range(i):
                    total_drop_if_break = 1 + j
                    total_drop_if_not_break = 1 + mem[i - j - 1]
                    total_drop = max(total_drop_if_break, total_drop_if_not_break)
                    if mem[i] is None or total_drop < mem[i]:
                        mem[i] = total_drop
        return mem[-1]

sol = Solution()
print(sol.twoEggDrop(1000))