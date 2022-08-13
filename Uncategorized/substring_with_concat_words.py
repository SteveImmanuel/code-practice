# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
from typing import List
from collections import Counter

class Solution:
    def find_all_idx(self, s, word):
        res = []
        idx = s.find(word)
        while idx != -1:
            res.append(idx)
            idx = s.find(word, idx+1)

        return set(res)

    def find_corresponding_word(self, index, occ_words):
        for key, val in occ_words.items():
            if index in val:
                return key

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        occ_words = {}
        unique_words = set(words)
        word_count = Counter(words)

        for word in unique_words:
            occ_words[word] = self.find_all_idx(s, word)
        
        if not all([len(item) > 0 for item in occ_words.values()]):
            return []
        # print(occ_words)
        occ_full_idx = set()
        for occ_word in occ_words.values():
            occ_full_idx = occ_full_idx.union(occ_word)

        occ_full_idx = sorted(list((occ_full_idx)))
        result = []
        # print(occ_full_idx)
        for i in range(len(occ_full_idx) - len(words) + 1):
            # print(i)
            word_count_temp = word_count.copy()
            current_idx = occ_full_idx[i]
            current_word = self.find_corresponding_word(current_idx, occ_words)
            # print(current_word)
            word_count_temp[current_word] -= 1
            for j in range(i+1, len(occ_full_idx)):
                # print(j)
                if occ_full_idx[j] == current_idx + word_len:
                    current_idx = occ_full_idx[j]
                    current_word = self.find_corresponding_word(current_idx, occ_words)
                    if word_count_temp[current_word] >= 1:
                        word_count_temp[current_word] -= 1
                    else:
                        break
                # else:
                #     break
            total_left = 0
            for val in word_count_temp.values():
                total_left += val
            if total_left == 0:
                result.append(occ_full_idx[i])
            # print(visitation)
            # print()

        return result

sol = Solution()
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
# s = "barfoothefoobarman"
# words = ["foo","bar"]
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","good"]
# s = "ababababab"
# words = ["ababa","babab"]
print(sol.findSubstring(s, words))
# print(sol.find_all_idx(s, words[0]))