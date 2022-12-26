class Solution:
    def is_perfect_square(self, n):
        i = 1
        while i*i < n:
            i += 1
        return i*i == n
    
    def numSquares(self, n: int) -> int:
        memory = [None for _ in range(n)]
        for i in range(n):
            number = i+1
            if self.is_perfect_square(number):
                memory[i] = 1
            else:
                if number%2 == 0 and memory[number//2 - 1] == 1:
                    memory[i] = 2
                else:
                    cur_min = None

                    j = 1
                    while j*j < number:
                        temp = memory[j*j - 1] + memory[number - j*j - 1]
                        
                        if cur_min is None or temp < cur_min:
                            cur_min = temp
                        j += 1
                    # for j in range(1, number//2 + 1):
                    #     temp = memory[j - 1] + memory[number - j - 1]
                        
                    #     if cur_min is None or temp < cur_min:
                    #         cur_min = temp
                    memory[i] = cur_min
                # return cur_min 
        return memory[-1]