class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occ = []
        for i in range(len(nums)):
            if nums[i] == x:
                occ.append(i)
        ans = []
        for q in queries:
            if q <= len(occ):
                ans.append(occ[q - 1])
            else:
                ans.append(-1)
        return ans