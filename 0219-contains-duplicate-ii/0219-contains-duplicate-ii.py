class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = defaultdict(lambda:[])
        for i, num in enumerate(nums):
            num_dict[num].append(i)
            
        for values in num_dict.values():
            if len(values) <= 1:
                continue
                
            for i in range(len(values)):
                for j in range(i+1, len(values)):
                    if abs(values[i] - values[j]) <= k:
                        return True
                    
        return False