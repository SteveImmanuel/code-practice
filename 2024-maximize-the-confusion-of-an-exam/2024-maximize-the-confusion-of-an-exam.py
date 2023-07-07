class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t_max = self.maxCons(answerKey, k, 'T')
        f_max = self.maxCons(answerKey, k, 'F')
        # print(t_max, f_max)
        return max(t_max, f_max)
    
    def maxCons(self, answerKey, k, changeTo):
        l, r = 0, 0
        budget = k
            
        max_cons = 1
        while r < len(answerKey):
            if answerKey[r] != changeTo:
                budget -= 1
            
            while budget < 0 and l <= r:
                if answerKey[l] != changeTo:
                    budget += 1
                l += 1
            
            max_cons = max(max_cons, r - l + 1)
            r += 1
        
        return max_cons
                
                