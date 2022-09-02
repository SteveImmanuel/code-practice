class PrefixTree:
    def __init__(self, char):
        self.char = char
        self.edges = {}
        self.is_word = False

    def add_edge(self, char):
        if char in self.edges:
            child = self.edges[char]
        else:
            child = PrefixTree(char)
            self.edges[char] = child
        return child

class Trie:
    def __init__(self):
        self.nodes = {}

    def insert(self, word: str) -> None:
        if word[0] in self.nodes:
            root = self.nodes[word[0]]
        else:
            root = PrefixTree(word[0])

        child = root
        for i in range(1, len(word)):
            child = child.add_edge(word[i])
        child.is_word = True
        self.nodes[word[0]] = root

    def search(self, word: str) -> bool:
        if word[0] not in self.nodes:
            return False
        
        node = self.nodes[word[0]]
        for i in range(1, len(word)):
            if word[i] in node.edges:
                node = node.edges[word[i]]
            else:
                return False
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self.nodes:
            return False
        
        node = self.nodes[prefix[0]]
        for i in range(1, len(prefix)):
            if prefix[i] in node.edges:
                node = node.edges[prefix[i]]
            else:
                return False
        return True
        
trie = Trie()
trie.insert("apple")
trie.insert("appra")
trie.insert("app")
# trie.insert("a")
# trie.search("apple")  
print(trie.search("app"))
print(trie.search("a"))
# trie.startsWith("app")
# trie.insert("app")
# trie.search("app")    
# print(trie.nodes['a'].edges['p'].edges['p'].edges)