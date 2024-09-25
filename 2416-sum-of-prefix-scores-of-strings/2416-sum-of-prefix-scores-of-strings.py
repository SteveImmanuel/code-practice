class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        pre_sum = defaultdict(int)
        for word in words:
            for i in range(1, len(word) + 1):
                key = word[:i]
                pre_sum[key] += 1
            
        answer = [0 for _ in range(len(words))]
        for j, word in enumerate(words):
            for i in range(1, len(word) + 1):
                key = word[:i]
                answer[j] += pre_sum[key]
        
        return answer
        