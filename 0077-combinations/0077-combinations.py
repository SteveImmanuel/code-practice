class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        choices = [i for i in range(1, n+1)]
        mem = {}
        result = self.combine_rec(0, choices, k, mem)
        return result
    
    
#     def combine_rec(self, start_idx, choices, k, mem):
#         if k == 1:
#             return [[x] for x in choices[start_idx:]]
#         else:
#             combine_rest = []
#             for i in range(start_idx + 1, len(choices) - k + 1):
#                 combine_rest += self.combine_rec(i + 1, choices, k - 1, mem)
#             print(combine_rest)
#             return list(map(lambda x: [choices[start_idx], *x], combine_rest))
            
        
#     # def combine_rec(self, choices, k, mem):
        
        
        
    def combine_rec(self, start_idx, choices, k, mem):
        key = (start_idx, k)
        
        if key not in mem:
            if k == 1:
                mem[key] = [[x] for x in choices[start_idx:]]
            else:
                result = []
                for i in range(start_idx + 1, len(choices) - k + 2):
                    combine_rest = self.combine_rec(i, choices, k - 1, mem)
                    result += list(map(lambda x: [choices[i - 1], *x], combine_rest))
                mem[key] = result
        return mem[key]