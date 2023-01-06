class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        queue = deque([(beginWord, 1)])
        
        while len(queue) > 0:
            cur_word, cur_length = queue.popleft()
            
            if cur_word == endWord:
                return cur_length
            self.get_next_valid(cur_word, cur_length, queue, word_set)
        
        return 0
        
    def get_next_valid(self, cur_word, cur_length, queue, word_set):
        for i in range(len(cur_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                candidate = cur_word[:i] + c + cur_word[i+1:]
                if candidate in word_set:
                    word_set.remove(candidate)
                    queue.append((candidate, cur_length+1))
