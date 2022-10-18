class Solution:
    def sort_string(self, text):
        return ''.join(sorted(list(text)))
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = map(lambda x:(x,self.sort_string(x)), strs)
        anagram_group = defaultdict(lambda: [])
        for text, sort_text in str_map:
            anagram_group[sort_text].append(text)
        return list(anagram_group.values())
