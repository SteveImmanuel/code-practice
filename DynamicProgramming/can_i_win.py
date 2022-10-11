# https://leetcode.com/problems/can-i-win/
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False
        
        mem = {}
        possible_choices = [i+1 for i in range(maxChoosableInteger)]
        self.canIWinRec(possible_choices, desiredTotal, mem)
        return mem[tuple(possible_choices)]

    def canIWinRec(self, possible_choices, total, mem):
        key = tuple(possible_choices)

        if key not in mem:
            if possible_choices[-1] >= total:
                mem[key] = True
            else:
                can_win = False
                for i in range(len(possible_choices)):
                    selected = possible_choices[i]
                    rest_choices = possible_choices[:i] + possible_choices[i+1:]
                    new_key = tuple(rest_choices)
                    if new_key not in mem:
                        self.canIWinRec(rest_choices, total-selected, mem)
                    can_win = can_win or not mem[new_key]
                    if can_win:
                        break
                
                mem[key] = can_win



sol = Solution()
print(sol.canIWin(10, 40))