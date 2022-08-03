# https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n <= 1:
            return 1
        else:
            gen_arr = [None] * (n+1)
            gen_arr[0] = 0
            gen_arr[1] = 1
            for i in range(2, n+1):
                if i%2 == 0:
                    gen_arr[i] = gen_arr[int(i//2)]
                else:
                    gen_arr[i] = gen_arr[int(i//2)] + gen_arr[int(i//2)+1]
        return max(gen_arr)

sol = Solution()
print(sol.getMaximumGenerated(7))