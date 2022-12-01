class Solution:
    def reorganizeString(self, s: str) -> str:
        occ = Counter(s)
        heap = [(-count, char) for char, count in occ.items()]
        heapq.heapify(heap)
        res = []
        
        while len(heap) > 0:
            item1 = heapq.heappop(heap)
            count1, char1 = -item1[0], item1[1]
            
            if len(heap) > 0:
                item2 = heapq.heappop(heap)
                count2, char2 = -item2[0], item2[1]
                res.append(char1)
                res.append(char2)
                count1 -= 1
                count2 -= 1
                if count1 > 0:
                    heapq.heappush(heap, (-count1, char1))
                if count2 > 0:
                    heapq.heappush(heap, (-count2, char2))
            else:
                if count1 == 1:
                    res.append(char1)
                else:
                    return ''
        
        return ''.join(res)
        