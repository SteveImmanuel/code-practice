class TrieNode:
    def __init__(self, val, children={}, is_word=False):
        self.val = val
        self.children = children
        self.is_word = is_word
        
    def add_word(self, word):
        cur_root = self
        for c in word:
            if c not in cur_root.children:
                new_child = TrieNode(c, {}, [])
                cur_root.children[c] = new_child
            cur_root = cur_root.children[c]
        cur_root.is_word = True
    
    def get_shortest(self, word):
        cur_root = self
        result = []
        for c in word:
            if c in cur_root.children:
                result.append(c)
                cur_root = cur_root.children[c]
                if cur_root.is_word:
                    return ''.join(result)
            else:
                return word
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        prefix_tree = TrieNode('', {}, [])
        for word in dictionary:
            prefix_tree.add_word(word)
        
        result = sentence.split(' ')
        for i in range(len(result)):
            result[i] = prefix_tree.get_shortest(result[i])
        
        return ' '.join(result)
