# https://leetcode.com/problems/reordered-power-of-2/

class Solution:
    def full_permutations(self, digits:str):
        if len(digits) == 1:
            return [digits]
        else:
            result = []
            for i in range(len(digits)):
                pivot = digits[i]
                rest = digits[:i] + digits[i+1:]
                rest_result = self.full_permutations(rest)
                for item in rest_result:
                    result.append(item+pivot)
            return result


    def is_power_2(self, n, mem):
        if n not in mem:
            if n == 1:
                mem[n] = True
                return True
            elif n%2 == 0:
                result = self.is_power_2(n//2, mem)
                mem[n] = result
            else:
                mem[n] = False
        
        return mem[n]
    
    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 1:
            return True
        str_n = str(n)
        all_perm = []
        for i in range(len(str_n)):
            if int(str_n[i]) % 2 == 0:
                rest = str_n[:i] + str_n[i+1:]
                perms = self.full_permutations(rest)
                for item in perms:
                    if item[0] != 0:
                        all_perm.append(item+str_n[i])


        all_perm = map(int, all_perm)
        mem = {}
        for item in all_perm:
            if self.is_power_2(item, mem):
                return True
        return False

sol = Solution()
print(sol.reorderedPowerOf2(16))