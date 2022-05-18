# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) <= 0:
            return []
            
        dict = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z'],
        }

        result = ['']
        for digit in digits:
            temp_result = result.copy()
            mapping = dict[digit]
            
            result = []
            for item in temp_result:
                for item2 in mapping:
                    result.append(item + item2)

            # print(result)
            # break
        return result

sol = Solution()
digits = '9999'
print(sol.letterCombinations(digits))
