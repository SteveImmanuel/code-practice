class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, i, j, path):
            char = board[i][j]
            curr_node = node.children.get(char)

            if not curr_node:
                return

            path += char
            if curr_node.is_end:
                result.add(path)
                curr_node.is_end = False  # Mark the word as visited

            temp, board[i][j] = board[i][j], "/"
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and board[x][y] != "/":
                    dfs(curr_node, x, y, path)
            board[i][j] = temp

        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                dfs(trie.root, i, j, "")

        return list(result)
