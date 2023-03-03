class Solution:
    def numSplits(self, s: str) -> int:
        left_dict = Counter(s[0])
        right_dict = Counter(s[1:])
        l = 1
        
        # print(left_dict, right_dict)
        if len(left_dict) > len(right_dict):
            return 0
        
        if len(left_dict) < len(right_dict):
            while l < len(s) and len(left_dict) != len(right_dict):
                left_dict[s[l]] += 1
                right_dict[s[l]] -= 1
                if right_dict[s[l]] == 0:
                    del right_dict[s[l]]
                l += 1
            
        total = 0    
        while l < len(s) and len(left_dict) == len(right_dict):
            total += 1
            left_dict[s[l]] += 1
            right_dict[s[l]] -= 1
            if right_dict[s[l]] == 0:
                del right_dict[s[l]]
            l += 1
        return total
            
        