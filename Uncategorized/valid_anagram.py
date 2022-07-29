# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1 = {}
        for char in s:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        
        for char in t:
            if char not in dict1:
                return False
            else:
                dict1[char] -= 1
        
        for value in dict1.values():
            if value != 0:
                return False
        
        return True



sol = Solution()
print(sol.isAnagram('a', 'b'))