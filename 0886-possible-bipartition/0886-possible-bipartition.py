class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislikes_dict = defaultdict(list)
        for a, b in dislikes:
            dislikes_dict[a].append(b)
            dislikes_dict[b].append(a)
            
        groups = [None] * n
        unchecked = set([i for i in range(1, n)])
        # queue = deque([(1, None)])
        queue = deque([])
        valid = True
        while len(unchecked) > 0 and valid:
            if len(unchecked) > 0:
                item = unchecked.pop()
                unchecked.add(item)
                queue.append((item, None))
            # print(queue)
            while len(queue) > 0 and valid:
                item, source = queue.popleft()
                if source is None:
                    groups[item - 1] = False
                else:
                    valid_group = not groups[source - 1]
                    if groups[item - 1] is None or groups[item - 1] == valid_group:
                        groups[item - 1] = valid_group
                    else:
                        valid = False

                if item in unchecked:
                    unchecked.remove(item)
                    for hate in dislikes_dict[item]:
                        queue.append((hate, item))
                # print(queue)
            
            
        # print(groups)
        return valid