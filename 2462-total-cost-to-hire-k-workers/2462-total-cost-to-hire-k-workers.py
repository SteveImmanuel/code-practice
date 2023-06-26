class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cost_with_idx = [(cost, i) for i, cost in enumerate(costs)]
        l_heap = cost_with_idx[:candidates]
        r_heap = cost_with_idx[-candidates:]
        heapq.heapify(l_heap)
        heapq.heapify(r_heap)
        l_idx = candidates
        r_idx = len(costs) - 1 - candidates
        
        total_cost = 0
        removed_idx = set()
        for i in range(k):
            min_l = l_heap[0]
            min_r = r_heap[0]
            
            if min_l[0] < min_r[0]:
                # print('l_small')
                
                total_cost += min_l[0]
                removed_idx.add(min_l[1])
                heapq.heappop(l_heap)
                while l_idx in removed_idx:
                    l_idx += 1
                if l_idx < len(costs):
                    heapq.heappush(l_heap, cost_with_idx[l_idx])
                    l_idx += 1
            elif min_l[0] > min_r[0]:
                # print('r_small')
                total_cost += min_r[0]
                removed_idx.add(min_r[1])
                
                heapq.heappop(r_heap)
                while r_idx in removed_idx:
                    r_idx -= 1
                if r_idx >= 0:
                    heapq.heappush(r_heap, cost_with_idx[r_idx])
                    r_idx -= 1
            else:
                if min_l[1] < min_r[1]:
                    # print('l_small tie')
                    
                    total_cost += min_l[0]
                    removed_idx.add(min_l[1])
                    
                    heapq.heappop(l_heap)
                    while l_idx in removed_idx:
                        l_idx += 1
                    if l_idx < len(costs):
                        heapq.heappush(l_heap, cost_with_idx[l_idx])
                        l_idx += 1
                elif min_l[1] > min_r[1]:
                    # print('r_small tie')
                    
                    total_cost += min_r[0]
                    removed_idx.add(min_r[1])
                    
                    heapq.heappop(r_heap)
                    while r_idx in removed_idx:
                        r_idx -= 1
                    if r_idx >= 0:
                        heapq.heappush(r_heap, cost_with_idx[r_idx])
                        r_idx -= 1
                else:
                    # print('tie')
                    total_cost += min_r[0]
                    removed_idx.add(min_r[1])
                    
                    heapq.heappop(r_heap)
                    heapq.heappop(l_heap)
                    
                    while l_idx in removed_idx:
                        l_idx += 1
                    while r_idx in removed_idx:
                        r_idx -= 1
                    if r_idx >= 0:
                        heapq.heappush(r_heap, cost_with_idx[r_idx])
                        r_idx -= 1
                    if l_idx < len(costs):
                        heapq.heappush(l_heap, cost_with_idx[l_idx])
                        l_idx += 1
            # print(l_heap, r_heap, total_cost)
        return total_cost