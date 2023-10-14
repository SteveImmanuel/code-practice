class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        
        result = []
        self.split(finalSum, result)
        # print(result)
        return result
        
    def split(self, remaining, result):
        if remaining == 0:
            return True
        
        start = 2
        if len(result) > 0:
            start = result[-1] + 2
            
        if remaining < start:
            return False
            
        for val in range(start, remaining + 1, 2):
            # print(remaining, val)
            result.append(val)
            found = self.split(remaining - val, result)
            if found:
                return True
            result.pop()