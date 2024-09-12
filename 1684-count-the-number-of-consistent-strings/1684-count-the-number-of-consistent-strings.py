class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        total = 0
        for word in words:
            x = set(word)
            if len(x.intersection(allowed)) == len(x):
                total += 1
        return total