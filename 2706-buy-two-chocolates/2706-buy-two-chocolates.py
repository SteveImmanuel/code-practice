class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        left = money - prices[0] - prices[1]
        return left if left >= 0 else money