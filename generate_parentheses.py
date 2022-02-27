# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        mem = {}
        return self.generateParenthesisRec(n, mem)

    def generateParenthesisRec(self, n: int, mem) -> List[str]:
        if n in mem:
            return mem[n]

        if n == 1:
            res = ['()']
        else:
            res = set()

            for i in range(1, n // 2 + 1):
                if i in mem:
                    first_term = mem[i]
                else:
                    first_term = self.generateParenthesisRec(i, mem)

                if n - i in mem:
                    second_term = mem[n - i]
                else:
                    second_term = self.generateParenthesisRec(n - i, mem)

                for gen1 in first_term:
                    for gen2 in second_term:
                        res.add(gen1 + gen2)
                        res.add(gen2 + gen1)

            if n - 1 in mem:
                nmin1_term = mem[n - 1]
            else:
                nmin1_term = self.generateParenthesisRec(n - 1, mem)

            for gen in nmin1_term:
                res.add('(' + gen + ')')

            res = list(res)

        mem[n] = res
        return res


sol = Solution()
x = 4
print(sol.generateParenthesis(x))

# ()
# ()() (())
# ()()() (()()) ()(()) (())() ((()))
# ()()()() ()(()()) (()())() ()()(()) ()(())() ()(())() (())()() ()((())) ((()))()