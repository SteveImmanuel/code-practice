class TrieNode:
    def __init__(self, val, children={}, index=[]):
        self.val = val
        self.children = children
        self.index = index
        
    def add_word(self, word, index):
        cur_root = self
        for c in word:
            if c not in cur_root.children:
                new_child = TrieNode(c, {}, [])
                cur_root.children[c] = new_child
            cur_root = cur_root.children[c]
            cur_root.index.append(index)
    
    def get_indices(self, word):
        cur_root = self
        for c in word:
            if c in cur_root.children:
                cur_root = cur_root.children[c]
            else:
                return []
        return cur_root.index
        

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        prefix_tree = TrieNode('', {}, [])
        result = sentence.split(' ')
        for i, word in enumerate(result):
            prefix_tree.add_word(word, i)
        
        for word in dictionary:
            indices = prefix_tree.get_indices(word)
            for item in indices:
                if len(word) < len(result[item]):
                    result[item] = word
        return ' '.join(result)
