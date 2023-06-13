import re

class Solution:
    def reverseWords(self, s: str) -> str:
        sanitized = re.sub(r'\s{2,}', ' ', s.strip())
        words = sanitized.split(' ')[::-1]
        return ' '.join(words)