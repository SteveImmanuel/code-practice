class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        occ1 = Counter(word1)
        occ2 = Counter(word2)
        
        occ1_val = sorted(list(occ1.values()))
        occ2_val = sorted(list(occ2.values()))        
        
        if len(occ1_val) != len(occ2_val):
            return False
        
        for i in range(len(occ1_val)):
            if occ1_val[i] != occ2_val[i]:
                return False
            
        word1_set = set(word1)
        word2_set = set(word2)
        
        return len(word1_set.difference(word2_set)) == 0
        