class Solution:
    def hIndex(self, citations) -> int:
        n = len(citations)
        l, r = 0, n
        max_citation = 0
        while l < r:
            m = (l + r) // 2
            total_paper = n - m
            if total_paper >= citations[m]:
                max_citation = max(max_citation, citations[m])
                l = m + 1
            else:
                r = m
            
            # break
        # total_paper = n - l
        # print(n, l)
        # print(l, r, citations[m], total_paper)
        # if l >= len(citations) or total_paper < citations[l]:
        #     l -= 1
        # print(n, l)
        return max(n - l, max_citation)