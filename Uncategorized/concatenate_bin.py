# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod_num = 1000000007

        sum = 0
        for i in range(1, n+1):
            lenth_bin = len(str(bin(i))[2:])
            sum = sum << lenth_bin
            sum += i
            sum %= mod_num
        return sum

sol = Solution()
print(sol.concatenatedBinary(12))