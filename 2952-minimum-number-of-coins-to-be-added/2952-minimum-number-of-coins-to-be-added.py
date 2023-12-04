class Solution(object):
    def minimumAddedCoins(self, coins, target):
        """
        :type coins: List[int]
        :type target: int
        :rtype: int
        """
        coin_sorted = sorted(coins)
        print(coin_sorted)
        largest_obtain = 0
        total_add = 0
        current_coin_idx = 0
        while largest_obtain < target:
            # print('b', largest_obtain, current_coin_idx, total_add)
            
            if current_coin_idx < len(coin_sorted):
                if coin_sorted[current_coin_idx] == largest_obtain + 1:
                    current_coin_idx += 1
                    largest_obtain = largest_obtain * 2 + 1
                else:
                    if coin_sorted[current_coin_idx] == 1:
                        current_coin_idx += 1
                        largest_obtain += 1
                    else:
                        total_add += 1
                        largest_obtain = largest_obtain * 2 + 1
            else:
                total_add += 1
                largest_obtain = largest_obtain * 2 + 1
            
            while current_coin_idx < len(coin_sorted) and coin_sorted[current_coin_idx] <= largest_obtain:
                largest_obtain += coin_sorted[current_coin_idx]
                current_coin_idx += 1
            # print('a', largest_obtain, current_coin_idx, total_add)
            # print('')
        return total_add