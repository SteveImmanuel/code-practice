class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        mem_dict = defaultdict(int)
        final_ans = 1
        for i, c in enumerate(s):
            if i == 0:
                mem_dict[c] = 1
            else:
                longest = 1
                for j in range(-k, k+1):
                    adj_c = chr(ord(c) + j)
                    # print(c, adj_c)
                    if adj_c in mem_dict:
                        longest = max(longest, 1 + mem_dict[adj_c])
                mem_dict[c] = longest
            final_ans = max(final_ans, mem_dict[c])
        # print(mem_dict)
    
        return final_ans