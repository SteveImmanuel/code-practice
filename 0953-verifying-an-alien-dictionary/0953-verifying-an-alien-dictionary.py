class Solution:
    def is_lsorted(self, word1, word2, order_dict):
        total = min(len(word1), len(word2))
        for i in range(total):
            if order_dict[word1[i]] < order_dict[word2[i]]:
                return True
            elif order_dict[word1[i]] > order_dict[word2[i]]:
                return False
        return len(word1) <= len(word2)
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {char:i for i, char in enumerate(order)}
        
        is_sorted = True
        i = 0
        while is_sorted and i < len(words) - 1:
            if not self.is_lsorted(words[i], words[i+1], order_dict):
                is_sorted = False
            i += 1
        return is_sorted
            