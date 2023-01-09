class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 1
        max_freq = 1
        occ_dict = Counter(s[:1])
        max_len = 1
        
        while end < len(s):
            occ_dict[s[end]] += 1
            max_freq = max(max_freq, occ_dict[s[end]])
            cur_window_size = end - start + 1
            if cur_window_size - max_freq > k:
                occ_dict[s[start]] -= 1
                start += 1
                
            max_len = max(max_len, end - start + 1)
            
            end += 1
        
        return max_len
        
                    
            
        