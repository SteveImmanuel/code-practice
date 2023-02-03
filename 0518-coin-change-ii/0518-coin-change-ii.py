class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        mem = [[None for _ in range(len(coins))] for _ in range(amount+1)]
               
        for i in range(amount+1):
            for j in range(len(coins)):
                if i == 0:
                    mem[i][j] = 0
                else:
                    total_combination = 0
                    remaining = i - coins[j]
                    if i % coins[j] == 0:
                        total_combination += 1
                    if remaining > 0:
                        total_combination += mem[remaining][j]
                        if remaining % coins[j] == 0:
                            total_combination -= 1
                    mem[i][j] = total_combination
            
            total = 0
            for j in range(len(coins)-1, -1, -1):
                total += mem[i][j]
                mem[i][j] = total
        # for a in mem:
        #     print(a)
        return mem[amount][0]