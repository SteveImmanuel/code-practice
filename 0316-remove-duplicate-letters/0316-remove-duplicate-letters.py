class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        occ = {}
        for i in range(len(s)):
            occ[s[i]] = i
            
        stack = []
        added = set()
        for i in range(len(s)):                
            if s[i] in added:
                continue
            
            while len(stack) > 0 and ord(stack[-1]) > ord(s[i]) and occ[stack[-1]] > i:
                added.discard(stack.pop())
            
            stack.append(s[i])
            added.add(s[i])
                
        return ''.join(stack)