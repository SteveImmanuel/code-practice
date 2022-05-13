# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        memory = [None] * len(s)

        for i in range(len(s)):
            if i == 0 or s[i] == s[i-1]:
                cur_len = 1
                temp_set = set(s[i])
                j = i + 1
            else:
                cur_len = memory[i - 1] - 1
                temp_set = set(s[i:i + cur_len])
                j = i + cur_len

            while j < len(s) and s[j] not in temp_set:
                temp_set.add(s[j])
                j += 1
                cur_len += 1
            memory[i] = cur_len
        
        return max(memory)

sol = Solution()
s = ''
print(sol.lengthOfLongestSubstring(s))