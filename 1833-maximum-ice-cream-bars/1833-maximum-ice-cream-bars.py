class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        total_ice = 0
        remaining_coins = coins
        
        for cost in sorted(costs):
            if remaining_coins >= cost:
                total_ice += 1
                remaining_coins -= cost
            else:
                break
        
        return total_ice