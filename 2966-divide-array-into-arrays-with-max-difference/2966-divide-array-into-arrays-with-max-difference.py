class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums_sorted = sorted(nums)
        # n_el = len(nums_sorted) // 3
        
        ans = []
        it = 0
        # for i in range(3):
        while it < len(nums_sorted):
            cur_min = nums_sorted[it]
            it += 1
            group = [cur_min]
            while len(group) < 3 and nums_sorted[it] - cur_min <= k:
                group.append(nums_sorted[it])
                it += 1
            
            if len(group) < 3:
                return []
            
            ans.append(group)
            # print(group)
        
        return ans
        
        
        