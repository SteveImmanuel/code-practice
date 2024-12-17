class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        string_dict = Counter(s)
        sorted_string = sorted(list(string_dict.keys()), reverse=True)
        new_dict = {}
        for i in range(len(sorted_string)):
            new_dict[i] = [sorted_string[i], string_dict[sorted_string[i]]]
        # print(new_dict)
        
        final_result = []
        idx = 0
        while idx < len(new_dict):
            next_idx = idx + 1
            while next_idx < len(new_dict) and new_dict[next_idx][1] == 0:
                next_idx += 1
            
            if next_idx == len(new_dict):
                next_idx = None
            
                
            while new_dict[idx][1] > 0:
                length = min(repeatLimit, new_dict[idx][1])
                final_result.append(new_dict[idx][0] * length)
                new_dict[idx][1] -= length
                
                if new_dict[idx][1] > 0:
                    if next_idx is not None:
                        final_result.append(new_dict[next_idx][0])
                        new_dict[next_idx][1] -= 1 
                        while next_idx < len(new_dict) and new_dict[next_idx][1] == 0:
                            next_idx += 1

                        if next_idx == len(new_dict):
                            next_idx = None
                    else:
                        break
            
            idx += 1
            while idx < len(new_dict) and new_dict[idx][1] == 0:
                idx += 1
                    
            # print(final_result)
            
        return ''.join(final_result)