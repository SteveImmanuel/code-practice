class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dist_dict = defaultdict(int)
        for x in arr:
            dist_dict[x] += 1
        cur_k = k
        for key, val in dist_dict.items():
            if val == 1:
                cur_k -= 1
            if cur_k == 0:
                return key
        return ''