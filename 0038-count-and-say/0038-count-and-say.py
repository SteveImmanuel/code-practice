class Solution:
    def convert_to_string(self, n):
        res = ''
        if len(n) <= 0:
            return ''
        
        count = 1
        current_char = n[0]
        for i in range(1, len(n)):
            if n[i] == current_char:
                count += 1
            else:
                res += f'{count}{current_char}'
                count = 1
                current_char = n[i]
        res += f'{count}{current_char}'
        return res
    
    def countAndSay(self, n: int) -> str:
        mem = [None] * n
        
        for i in range(n):
            if i == 0:
                mem[i] = '1'
            else:
                mem[i] = self.convert_to_string(mem[i-1])
        
        return mem[-1]
        