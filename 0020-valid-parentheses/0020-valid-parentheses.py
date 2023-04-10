class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last_item = stack.pop()
                if (char == ')' and last_item != '(') or (char == '}' and last_item != '{') or (char == ']' and last_item != '['):
                    return False
        
        return len(stack) == 0