class Solution:
    def divisorGame(self, n: int) -> bool:
        outcome = [i%2==1 for i in range(n)]
        return outcome[-1]