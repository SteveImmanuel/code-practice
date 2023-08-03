class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        mem = [None] * len(questions)
        
        for i in range(len(questions) - 1, -1 , -1):
            if i == len(questions) - 1:
                mem[i] = questions[i][0]
            else:
                # case answer
                total = questions[i][0]
                if i + questions[i][1] + 1 < len(questions):
                    total += mem[i + questions[i][1] + 1]
                mem[i] = max(mem[i+1], total)
        
        return max(mem)
                
            