class Solution:
    def minimumPushes(self, word: str) -> int:
        letter = Counter(word)
        letter = sorted(letter.items(), key=lambda x: -x[1])
        # print(letter)
        cost = 1
        total = 0
        for i in range(0, len(letter), 8):
            for j in range(i, i+8):
                if j >= len(letter):
                    return total
                total += letter[j][1] * cost
            cost += 1
        return total