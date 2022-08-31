# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ''
        step_size = (numRows-1) * 2
        step_size_alt = 0
        
        for i in range(numRows):
            iter = i
            
            if i == 0 or i == numRows - 1:
                step_size = (numRows-1) * 2
                while iter < len(s):
                    res += s[iter]
                    iter += step_size
            else:
                step_size_alt += 2
                step_size -= 2
                switch = True
                while iter < len(s):
                    res += s[iter]
                    if switch:
                        iter += step_size
                    else:
                        iter += step_size_alt
                    switch = not switch
        return res

sol = Solution()
s = 'PAYPALISHIRING'
numRows = 1
print(sol.convert(s, numRows))