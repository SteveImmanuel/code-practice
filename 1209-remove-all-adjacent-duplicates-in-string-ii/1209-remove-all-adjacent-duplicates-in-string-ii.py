class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append((char, 1))
            else:
                if stack[-1][0] == char:
                    if stack[-1][1] == k-1:
                        for _ in range(k-1):
                            stack.pop()
                    else:
                        stack.append((char, stack[-1][1] + 1))
                else:
                    stack.append((char, 1))
        return ''.join(map(lambda x:x[0], stack))
        