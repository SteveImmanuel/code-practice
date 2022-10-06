# https://leetcode.com/problems/powx-n/description/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # mem = {}
        # res = self.myPowRec(x, n, mem)
        return self.myPowRec(x, n, {})

    def myPowRec(self, x: float, n: int, mem) -> float:
        if n not in mem:
            if n == 1:
                mem[n] = x
            elif n == 0:
                mem[n] = 1
            else:
                pow = abs(n)

                if pow%2 == 0:
                    pow1 = pow2 = pow//2
                else:
                    pow1 = (pow+1) // 2
                    pow2 = (pow-1) // 2
                res = self.myPowRec(x, pow1, mem) * self.myPowRec(x, pow2, mem)
                if n < 0:
                    res = 1/res
                mem[n] = res
        return mem[n]

sol = Solution()
print(sol.myPow(2, 10))