class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans = [x.split(',') for x in transactions]
        trans = [(a, int(b), int(c), d) for a, b, c, d in trans]
        invalid = []
        for i, t in enumerate(transactions):
            if trans[i][2] > 1000:
                invalid.append(t)
            else:
                for j in range(len(trans)):
                    if j != i:
                        if abs(trans[i][1] - trans[j][1]) <= 60 and trans[i][0] == trans[j][0] and trans[i][3] != trans[j][3]:
                            if t == 'bob,536,217,toronto':
                                print(trans[i], trans[j])
                            invalid.append(t)
                            break
        return invalid