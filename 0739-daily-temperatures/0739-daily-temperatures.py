class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [None] * len(temperatures)
        answer[-1] = 0
        
        min_stack = [(temperatures[-1], len(temperatures) - 1)]
        for i in range(len(temperatures) - 2, -1, -1):
            
            if temperatures[i] < min_stack[-1][0]:
                answer[i] = min_stack[-1][1] - i
            else:
                while len(min_stack) > 0 and min_stack[-1][0] <= temperatures[i]:
                    min_stack.pop()
                
                if len(min_stack) == 0:
                    answer[i] = 0
                else:
                    answer[i] = min_stack[-1][1] - i
                
            if len(min_stack) == 0 or temperatures[i] <= min_stack[-1][0]:
                min_stack.append((temperatures[i], i))
        return answer
                