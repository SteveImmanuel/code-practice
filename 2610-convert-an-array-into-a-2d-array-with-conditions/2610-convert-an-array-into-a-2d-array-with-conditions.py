class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        occ = list(Counter(nums).items())
        occ.sort(key=lambda x: -x[1])
        
        result = [[] for _ in range(occ[0][1])]
        
        for num, val in occ:
            for i in range(val):
                result[i].append(num)
        
        return result