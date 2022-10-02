# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mem = {}
        return self.numRollsToTargetRec(n, k, target, mem)
        
    def numRollsToTargetRec(self, n: int, k: int, target: int, mem) -> int:
        key = (n, target)
        if key not in mem:
            if n == 1:
                if 0 < target <= k:
                    mem[key] = 1
                else:
                    mem[key] = 0
            else:
                total = 0

                for i in range(1, min(target, k+1)):
                    tail_res = self.numRollsToTargetRec(n-1, k, target - i, mem)
                    if tail_res != 0:
                        total += tail_res % 1000000007
                
                mem[key] = total % 1000000007
        return mem[key]



sol = Solution()
n = 1
k = 6
target = 3
n = 2
k = 6
target = 7
n = 30
k = 30
target = 500
print(sol.numRollsToTarget(n, k, target))