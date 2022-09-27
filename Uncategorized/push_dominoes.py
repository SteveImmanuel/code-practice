# https://leetcode.com/problems/push-dominoes/
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        left_val = [None] * len(dominoes)
        right_val = [None] * len(dominoes)
        
        val = 0
        for i in range(len(dominoes)):
            if dominoes[i] == '.':
                if val == 0:
                    right_val[i] = 0
                else:
                    right_val[i] = val
                    val += 1
            elif dominoes[i] == 'R':
                val = 1
            elif dominoes[i] == 'L':
                val = 0

        val = 0
        for i in range(len(dominoes) - 1, -1, -1):
            if dominoes[i] == '.':
                if val == 0:
                    left_val[i] = 0
                else:
                    left_val[i] = val
                    val += 1
            elif dominoes[i] == 'L':
                val = 1
            elif dominoes[i] == 'R':
                val = 0

        res = ''
        for i in range(len(dominoes)):
            if left_val[i] is None: # and right_val[i] is None
                res += dominoes[i]
            else:
                if left_val[i] == right_val[i]:
                    res += '.'
                elif left_val[i] < right_val[i]:
                    if left_val[i] != 0:
                        res += 'L'
                    else:
                        res += 'R'
                elif right_val[i] < left_val[i]:
                    if right_val[i] != 0:
                        res += 'R'
                    else:
                        res += 'L'
        return res
        
sol = Solution()
dominoes = ".L.R...LR..L.."
dominoes = "RR.L"
print(sol.pushDominoes(dominoes))