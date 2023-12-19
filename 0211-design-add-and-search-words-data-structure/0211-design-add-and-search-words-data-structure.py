class TreeNode:
    def __init__(self, char, children, is_word):
        self.char = char
        self.children = children
        self.is_word = is_word

class WordDictionary:

    def __init__(self):
        self.tree = TreeNode('0', {}, False)

    def addWord(self, word: str) -> None:
        self._insert(word, 0, self.tree)
        
    def _insert(self, word, idx, cur_node):
        if idx >= len(word):
            return
        
        char = word[idx]
        is_word = idx == len(word) - 1
        if char not in cur_node.children:
            cur_node.children[char] = TreeNode(char, {}, is_word)
        else:
            cur_node.children[char].is_word = cur_node.children[char].is_word or is_word
            
        self._insert(word, idx + 1, cur_node.children[char])
            
    def search(self, word: str) -> bool:
        return self._search(word, 0, self.tree)
    
    def _search(self, word, idx, cur_node):
        char = word[idx]
        if idx == len(word) - 1:
            if char != '.':
                return char in cur_node.children and cur_node.children[char].is_word
            else:
                for child in cur_node.children:
                    if cur_node.children[child].is_word:
                        return True
                return False
        else:
            if char != '.':
                if char not in cur_node.children:
                    return False
                return self._search(word, idx + 1, cur_node.children[char])
            else:
                for child in cur_node.children:
                    if self._search(word, idx + 1, cur_node.children[child]):
                        return True
                return False