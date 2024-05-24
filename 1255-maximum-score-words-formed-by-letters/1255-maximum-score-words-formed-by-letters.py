class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        res = 0
        for mask in range(1, 2**len(words)):
            occ = Counter(letters)
            cur_total = 0
            i = len(words) - 1
            valid = True
            while mask > 0 and valid:
                if mask & 1 == 1:
                    for c in words[i]:
                        if occ[c] > 0:
                            occ[c] -= 1
                            cur_total += score[ord(c) - 97]
                        else:
                            valid = False
                            break
                mask >>= 1
                i -= 1
            if valid:
                res = max(res, cur_total)
        return res