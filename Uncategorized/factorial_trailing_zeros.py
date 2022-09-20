# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    # def trailingZeroes(self, n: int) -> int:
    #     # max_tens = len(str(n)) - 1
    #     max_fives = len(str(n)) + 1
        
    #     total_zeros = 0
    #     # cummulative_sum = 0
    #     # tens = []
    #     # for i in range(max_tens, 0, -1):
    #     #     divisor = 10 ** i
    #     #     div_res = n // divisor
    #     #     print(divisor, div_res, cummulative_sum)
    #     #     total_zeros += (div_res - cummulative_sum) * i
    #     #     tens.insert(0, (div_res - cummulative_sum))
    #     #     cummulative_sum += div_res
    #     # print(total_zeros)
    #     # print(tens)
    #     cummulative_sum = 0
    #     for i in range(max_fives, 0, -1):
    #         div_res = n // (5 ** i)
    #         # if div_res > 0:
    #         #     if div_res % 2 == 0:
    #         #         div_res = div_res // 2
    #         #     else:
    #         #         div_res = (div_res // 2) + 1
    #         total_zeros += (div_res - cummulative_sum) * i
    #         print(5 ** i, div_res, cummulative_sum, total_zeros)
    #         cummulative_sum += div_res
        
    #     return total_zeros

    def trailingZeroes(self, n: int) -> int:
        if n <= 1:
            return 0
        total = 0
        num = n

        n, mod = divmod(n, 5)
        while mod == 0:
            total += 1
            n, mod = divmod(n, 5)
        return total + self.trailingZeroes(num-1)


    

sol = Solution()
print(sol.trailingZeroes(234))

# 1234
# 3245
# 9999
# 3456
# 234
# 52

# 245
# 646
# 1990
# 688
# 46
# 10

# 305
# 809
# 2495
# 862
# 56
# 12