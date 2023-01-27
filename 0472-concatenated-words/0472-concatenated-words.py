class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        mem = {}
        word_set = set(words)
        res = []
        
        for word in words:
            self.is_possible(word, word_set, mem)
            # print(mem)
        for word, possible in mem.items():
            if possible and word in word_set:
                res.append(word)
        return res
        
    def is_possible(self, word, word_set, mem):
        if word not in mem:
            is_possible = False
            for i in range(1, len(word)):
                head = word[:i]
                tail = word[i:]
                
                # print(head, tail, word)
                if head in word_set and (tail in word_set or self.is_possible(tail, word_set, mem)):
                    # print(head, tail, word)
                    
                    is_possible = True
                    break
                    
            mem[word] = is_possible
        
        return mem[word]
        