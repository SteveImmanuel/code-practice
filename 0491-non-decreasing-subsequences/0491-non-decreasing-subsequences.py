class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subseq_dict = {}
        
        for i in range(len(nums) - 1, -1, -1):
            cur_res = [[nums[i]]]
            seen = set()
            for j in range(i + 1, len(nums)):
                if nums[j] not in seen and nums[j] >= nums[i]:
                    seen.add(nums[j])
                    for item in subseq_dict[nums[j]]:
                        cur_res.append([nums[i]] + item)
            subseq_dict[nums[i]] = cur_res
        
        res = []
        for key, value in subseq_dict.items():
            for i in range(len(value)):
                if i > 0:
                    res.append(value[i])
        return res
    