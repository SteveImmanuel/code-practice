class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_dict = {}
        pattern_used = set()
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        for p, word in zip(pattern, words):
            if word not in word_dict:
                if p not in pattern_used:
                    word_dict[word] = p
                    pattern_used.add(p)
                else:
                    return False
            else:
                if word_dict[word] != p:
                    return False
        return True