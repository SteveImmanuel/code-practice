class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        memories = defaultdict(lambda : defaultdict(lambda : [0, 0]))
        for i in range(len(nums)):
            has_seen = set()
            for j in range(i):
                if nums[j] not in has_seen:
                    has_seen.add(nums[j])
                    diff = nums[i] - nums[j]
                    memories[nums[i]][diff][0] += memories[nums[j]][diff][0] + memories[nums[j]][diff][1]
            
            for j in range(i):
                diff = nums[i] - nums[j]
                memories[nums[i]][diff][1] += 1

        total = 0
        for key in memories.keys():
            for ikey in memories[key].keys():
                total += memories[key][ikey][0]
        return total