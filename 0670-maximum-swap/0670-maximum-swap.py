class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        for i in range(len(num_list)):
            if num_list[i] == '9':
                continue
            
            max_idx = -1
            for j in range(i+1, len(num_list)):
                if num_list[j] > num_list[i] and (max_idx == -1 or num_list[j] >= num_list[max_idx]):
                    max_idx = j
            # print(i, num_list[i], max_idx, num_list[max_idx])
            if max_idx != -1:
                num_list[i], num_list[max_idx] = num_list[max_idx], num_list[i]
                break
            # print(num_list)
            
        return int(''.join(num_list))
                