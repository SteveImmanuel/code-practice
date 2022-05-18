# https://leetcode.com/problems/can-i-win/
# NOT DONE
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        return self.canIWinRec([i+1 for i in range(maxChoosableInteger)], desiredTotal)

    def canIWinRec(self, pool, desiredTotal):
        print(pool, desiredTotal, end=' ')
        min_choosable = pool[0]
        max_choosable = pool[-1]

        if desiredTotal <= max_choosable:
            print('choose', max_choosable)
            return True
        else:
            print('choose', min_choosable)
            pool.pop(0)
            return not self.canIWinRec(pool, desiredTotal-min_choosable)



sol = Solution()
print(sol.canIWin(10, 40))