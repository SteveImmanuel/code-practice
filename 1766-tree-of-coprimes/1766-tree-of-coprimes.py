class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        coprimes_dict = defaultdict(set)
        for i in range(1, 51):
            for j in range(1, 51):
                if self.gcd(i, j) == 1:
                    coprimes_dict[i].add(j)

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        node_dict = {i: x for i, x in enumerate(nums)}
        parent_dict = defaultdict(list)
        res = [None] * len(nums)
        visited = set()
        self.traverse(0, node_dict, parent_dict, coprimes_dict, graph, visited, res, 0)
        return res
        
    def traverse(self, cur_node, node_dict, parent_dict, coprimes_dict, graph, visited, res, counter):
        visited.add(cur_node)
        node_val = node_dict[cur_node]
        parent_id = (-1, -1)
        possible_coprimes = coprimes_dict[node_val]
        for x in possible_coprimes:
            if x in parent_dict and len(parent_dict[x]) > 0 and parent_dict[x][-1][1] > parent_id[1]:
                parent_id = parent_dict[x][-1]
        # print(cur_node, parent_id, parent_dict)
        res[cur_node] = parent_id[0]
                    
        parent_dict[node_val].append((cur_node, counter))
        for child in graph[cur_node]:
            if child not in visited:
                self.traverse(child, node_dict, parent_dict, coprimes_dict, graph, visited, res, counter+1)
        parent_dict[node_val].pop()
            
    
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)