# https://leetcode.com/problems/coin-change/description/
from typing import List

class Solution:
    # TIME LIMIT EXCEEDED
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     memory = []
    #     for _ in range(amount+1):
    #         memory.append([None] * (len(coins)+1))

    #     for i in range(len(memory)):
    #         for j in range(len(coins)):
    #             if i == 0:
    #                 memory[i][j] = 0
    #             else:
    #                 min_amount = None

    #                 for k in range(i):
    #                     remaining = i - k

    #                     cur_min_amount = None
    #                     if remaining % coins[j] == 0 and memory[k][len(coins)] is not None:
    #                         cur_min_amount = remaining // coins[j] + memory[k][len(coins)]
    #                         if min_amount is None or cur_min_amount < min_amount:
    #                             min_amount = cur_min_amount

    #                 memory[i][j] = min_amount                            

    #         arr = [x for x in memory[i] if x is not None]
    #         if len(arr) > 0:
    #             memory[i][len(coins)] = min(arr)
        
    #     if memory[amount][len(coins)] is None:
    #         return -1
    #     return memory[amount][len(coins)]

    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     memory = [amount + 1] * (amount + 1)
    #     memory[0] = 0

    #     for i in range(len(memory)):
    #         for j in range(len(coins)):
    #             if coins[j] > i:
    #                 continue
    #             else:
    #                 remaining = i - coins[j]
    #                 memory[i] = min(memory[i], memory[remaining] + 1)         

    #     return memory[amount] if memory[amount] != (amount + 1) else -1 

    def coinChange(self, coins: List[int], amount: int) -> int:
        memory = []
        for _ in range(amount+1):
            memory.append([None] * (len(coins)+1))

        for i in range(len(memory)):
            for j in range(len(coins)):
                if i == 0:
                    memory[i][j] = 0
                elif coins[j] > i:
                    continue
                else:
                    min_amount = None
                    remaining = i - coins[j]

                    if i % coins[j] == 0:
                        min_amount = i // coins[j]
                    
                    if memory[remaining][len(coins)] is not None:
                        if min_amount is None:
                            min_amount = 1 + memory[remaining][len(coins)]
                        else:
                            min_amount = min(min_amount, 1 + memory[remaining][len(coins)])

                    memory[i][j] = min_amount                            

            arr = [x for x in memory[i] if x is not None]
            if len(arr) > 0:
                memory[i][len(coins)] = min(arr)
        
        if memory[amount][len(coins)] is None:
            return -1
        return memory[amount][len(coins)]
        

sol = Solution()
coins = [186,419,83,408]
amount = 6249
print(sol.coinChange(coins, amount))