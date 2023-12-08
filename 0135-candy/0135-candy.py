class Solution:
    def candy(self, ratings: List[int]) -> int:
        rating_idx = [(i, c) for i, c in enumerate(ratings)]
        rating_idx.sort(key=lambda x:x[1])
        candy = [1] * len(ratings)
        for i, _ in rating_idx:
            c = 1
            if i > 0 and ratings[i] > ratings[i-1]:
                c = max(c, candy[i-1] + 1)
            if i < len(ratings) - 1 and ratings[i] > ratings[i+1]:
                c = max(c, candy[i+1] + 1)
            candy[i] = c
        return sum(candy)