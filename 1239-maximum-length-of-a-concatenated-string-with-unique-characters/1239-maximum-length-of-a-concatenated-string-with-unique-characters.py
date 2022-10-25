class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr_filtered = map(lambda x: set(x) if len(set(x)) == len(x) else '', arr)
        arr_filtered = list(filter(lambda x: x != '', arr_filtered))
        if len(arr_filtered) == 0:
            return 0
        
        total_possible = []
        
        for i in range(len(arr_filtered)):
            if i == 0:
                total_possible.append(arr_filtered[i])
            else:
                len_total_possible = len(total_possible)
                total_possible.append(arr_filtered[i])
                
                for j in range(len_total_possible):
                    # cur_set = arr_filtered[i]
                    # max_set = arr_filtered[i]
                    # for j in range(i):
                    concat_len = len(total_possible[j]) + len(arr_filtered[i])
                    union = total_possible[j].union(arr_filtered[i]) 
                    if concat_len == len(union):
                        total_possible.append(union)
        #     print(i, len(total_possible))
        # print(total_possible, len(total_possible))
        return max(map(lambda x:len(x), total_possible))