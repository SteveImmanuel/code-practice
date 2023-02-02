class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        possible = [False, False, False]
        ta, tb, tc = target
        for a, b, c in triplets:
            if a == ta and b <= tb and c <= tc:
                possible[0] = True
            if a <= ta and b == tb and c <= tc:
                possible[1] = True
            if a <= ta and b <= tb and c == tc:
                possible[2] = True
        return all(possible)
                