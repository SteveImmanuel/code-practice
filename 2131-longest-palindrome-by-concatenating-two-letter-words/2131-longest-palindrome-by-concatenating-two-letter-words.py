class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_dict = Counter(words)
        
        max_len = 0
        no_pair_used = True
        for word in words:
            if word not in word_dict:
                continue
                
            word_dict[word] -= 1
            if word_dict[word] == 0:
                del word_dict[word]
            
            reverse_word = word[::-1]
            if reverse_word in word_dict:
                word_dict[reverse_word] -= 1
                if word_dict[reverse_word] == 0:
                    del word_dict[reverse_word]
                
                max_len += 4
            elif reverse_word == word and no_pair_used:
                no_pair_used = False
                max_len += 2
        
        return max_len