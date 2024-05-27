class Solution:
    def specialArray(self, nums: List[int]) -> int:
        occ = Counter(nums)
        keys = sorted(list(occ.keys()))
        cumsum = [None] * len(keys)
        total = 0
        for i in range(len(cumsum) - 1, -1, -1):
            total += occ[keys[i]]
            cumsum[i] = total
        # print(keys, cumsum)
        for i in range(len(keys)):
            # print(keys[i], cumsum[i])
            if keys[i] == cumsum[i]:
                return cumsum[i]
            else:
                if i > 0:
                    if keys[i] > cumsum[i] and cumsum[i] > keys[i-1]:
                        return cumsum[i]
                else:
                    if keys[i] > cumsum[i]:
                        return cumsum[i]
                        
        return -1