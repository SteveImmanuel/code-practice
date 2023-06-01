class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for i in range(len(citations) - 1, -1, -1):
            if citations[i] >= i + 1:
                h_index = i + 1
                break
        return h_index