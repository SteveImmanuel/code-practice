class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_occ = Counter(words)
        word_occ_items = list(word_occ.items())
        word_occ_items.sort(key=lambda x:(-x[1],x[0]))
        # print(word_occ_items)
        return list(map(lambda x:x[0], word_occ_items[:k]))