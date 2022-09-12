# https://leetcode.com/problems/bag-of-tokens/
from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        sorted_tokens = sorted(tokens)

        if len(sorted_tokens) > 0 and sorted_tokens[0] <= power:
            power -= sorted_tokens.pop(0)
            score += 1

            valid = True
            while valid:
                valid = False

                total_power = 0
                i = 0
                while i < len(sorted_tokens) and total_power + sorted_tokens[i] <= power:
                    total_power += sorted_tokens[i]
                    i += 1

                sorted_tokens = sorted_tokens[i:]
                power -= total_power
                score += i

                if score >= 0 and len(sorted_tokens) > 0:
                    biggest_power = sorted_tokens.pop()
                    if len(sorted_tokens) > 0 and power + biggest_power >= sorted_tokens[0]:
                        score -= 1
                        power += biggest_power
                        valid = True
        
        return score

sol = Solution()
tokens = [100]
power = 50
tokens = [100,200]
power = 150
tokens = [100,200,300,400]
power = 200
print(sol.bagOfTokensScore(tokens, power))        