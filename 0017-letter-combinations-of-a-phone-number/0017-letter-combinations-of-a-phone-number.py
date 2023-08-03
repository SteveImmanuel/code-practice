class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return letter_dict[digits]
        else:
            result = []
            remaining_combination = self.letterCombinations(digits[1:])
            for letter in letter_dict[digits[0]]:
                for item in remaining_combination:
                    result.append(letter + item)
            return result
        
