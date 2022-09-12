# https://leetcode.com/problems/count-vowels-permutation/

from functools import total_ordering


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        char_dict = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
        total_char = 1

        while total_char < n:
            new_dict = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
            #a
            new_dict['e'] += char_dict['a']
            #e
            new_dict['a'] += char_dict['e']
            new_dict['i'] += char_dict['e']
            #i
            new_dict['a'] += char_dict['i']
            new_dict['e'] += char_dict['i']
            new_dict['o'] += char_dict['i']
            new_dict['u'] += char_dict['i']
            #o
            new_dict['i'] += char_dict['o']
            new_dict['u'] += char_dict['o']
            #u
            new_dict['a'] += char_dict['u']

            char_dict = new_dict
            total_char += 1

        total = 0
        for val in char_dict.values():
            if total > (1000000007):
                total %= 1000000007
            total += val
        return total % 1000000007

sol = Solution()
print(sol.countVowelPermutation(5))