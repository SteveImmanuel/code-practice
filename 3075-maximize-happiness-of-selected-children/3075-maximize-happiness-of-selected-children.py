class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        selected = happiness[:k]
        # print(selected)
        reduce = [i for i in range(len(selected))]
        final_selected = [max(0, s - r) for s, r in zip(selected, reduce)]
        # print(final_selected)
        return sum(final_selected)