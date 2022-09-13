# https://leetcode.com/problems/utf-8-validation/
from typing import List

class Solution:
    def get_byte(self, num):
        binary = str(bin(num))[2:]
        return binary.zfill(8)[-8:]
    
    def count_one(self, str_num):
        total = 0
        i = 0
        while i < len(str_num) and str_num[i] == '1':
            total += 1
            i += 1
        return total

    def validUtf8(self, data: List[int]) -> bool:

        bytes = list(map(self.get_byte, data))
        i = 0
        valid = True
        first = True
        print(bytes)
        while i < len(bytes) and valid:
            if first:
                first = bytes[i].startswith('0')
                total_tail = self.count_one(bytes[i]) - 1
                valid = not bytes[i].startswith('10') and total_tail <= 3
                print(total_tail)
            else:
                valid = bytes[i].startswith('10') and total_tail > 0
                total_tail -= 1
                first = total_tail == 0
            i += 1
        print(total_tail)
        return valid and i == len(bytes) and (total_tail == 0  or total_tail == -1)


sol = Solution()
# data = [235,140,4]
# data = [197,130]
data = [255]
data = [145]
data = [250,145,145,145,145]
data = [228,189,160,229,165,189,13,10]
print(sol.validUtf8(data))