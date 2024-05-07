class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = [a, b, c]
        stones.sort()
        max_move = stones[-1] - stones[0] - 2
        if stones[1] - 1 == stones[0] and stones[1] + 1 == stones[2]:
            min_move = 0
        elif stones[1] - 1 == stones[0] or stones[1] + 1 == stones[2]:
            min_move = 1
        elif stones[1] - 2 == stones[0] or stones[1] + 2 == stones[2]:
            min_move = 1
        else:
            min_move = 2
        return [min_move, max_move]