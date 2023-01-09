class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        max_len = 1
        start = 0
        cur_set = set([s[start]])
        end = 1
        
        while end < len(s):
            if s[end] not in cur_set:
                cur_set.add(s[end])
            else:
                while s[end] in cur_set:
                    cur_set.remove(s[start])
                    start += 1
                cur_set.add(s[end])
                
            end += 1
            max_len = max(max_len, len(cur_set))
        
        return max_len
        