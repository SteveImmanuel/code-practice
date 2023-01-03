class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        mem = [[] for _ in range(len(nums))] 
        
        for i in range(len(nums)):
            if i == 0:
                mem[i] = [(1, '*')]
            elif i == 1:
                if nums[i] != nums[0]:
                    mem[i] = [(2, '<' if nums[i] > nums[0] else '>')]
                else:
                    mem[i] = [(1, '*')]
            else:
                max_more = 1
                max_less = 1
                # print(mem[i])
                for j in range(i):
                    for total, sign in mem[j]:
                        if sign == '*':
                            if nums[i] > nums[j]:
                                max_more = max(max_more, total + 1)
                            elif nums[i] < nums[j]:
                                max_less = max(max_less, total + 1)
                        elif sign == '>' and nums[i] > nums[j]:
                            max_more = max(max_more, total + 1)
                        elif sign == '<' and nums[i] < nums[j]:
                            max_less = max(max_less, total + 1)
                    
                if max_more > 1:
                    mem[i].append((max_more, '<'))
                if max_less > 1:
                    mem[i].append((max_less, '>'))
                if max_more == 1 or max_less == 1:
                    mem[i].append((1, '*'))
            
        return max(map(lambda x:x[0], mem[-1]))
                        
