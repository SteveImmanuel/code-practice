class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = Counter(arr)
        occ_val = list(occ.values())
        return len(occ_val) == len(set(occ_val))