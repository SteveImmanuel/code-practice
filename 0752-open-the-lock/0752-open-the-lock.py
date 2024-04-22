class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([('0000', 0)])
        min_cost = float('inf')
        deadends = set(deadends)
        
        visited = set()
        while len(queue) > 0:
            cur_num, cur_cost = queue.popleft()
            if cur_num in deadends:
                continue
            # print(cur_num in visited)
            if cur_num == target:
                min_cost = min(min_cost, cur_cost)
            else:
                for i in range(4):
                    for j in [-1, 1]:
                        new_digit = (int(cur_num[i]) + j) % 10
                        new_num = cur_num[:i] + str(new_digit) + cur_num[i+1:]
                        # print(new_num, len(visited), len(queue))
                        if new_num not in visited:
                            visited.add(new_num)
                            queue.append((new_num, cur_cost + 1))
        
        if min_cost == float('inf'):
            return -1
        return min_cost